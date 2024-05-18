import json
import tqdm
import os
import random
from datetime import datetime
import argparse
import time

from langchain_community.llms import HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()


def make_requests(
        engine, prompts, max_tokens, temperature, top_p, frequency_penalty, presence_penalty, stop_sequences,
        logprobs, n, best_of, retries=3, api_key=None, organization=None
):
    llm_model = HuggingFaceEndpoint(repo_id=engine, temperature=temperature, top_p=top_p,
                                    model_kwargs={'input': prompts, 'max_tokens': max_tokens,
                                                  'frequency_penalty': frequency_penalty,
                                                  'presence_penalty': presence_penalty, 'stop': stop_sequences,
                                                  'logprobs': logprobs, 'n': n, 'best_of': best_of})
    response = None
    if api_key is not None:
        llm_model.api_key = api_key
    if organization is not None:
        llm_model.organization = organization
    retry_cnt = 0
    backoff_time = 30
    while retry_cnt <= retries:
        try:
            llm_res = []
            for p in prompts:
                res = llm_model.invoke(input=p)
                llm_res.append(res)
            response = {
                "choices": []
            }
            for prompt, generated_text in zip(prompts, llm_res):
                response["choices"].append({
                    "prompt": prompt,
                    "generated_text": generated_text
                })
            break
        except Exception as e:
            print(f"MixtralError: {e}.")
            print(f"Retrying in {backoff_time} seconds...")
            time.sleep(backoff_time)
            backoff_time *= 1.5
            retry_cnt += 1

    if isinstance(prompts, list):
        results = []
        for j, prompt in enumerate(prompts):
            data = {
                "prompt": prompt,
                "response": {"choices": response["choices"][j * n: (j + 1) * n]} if response else None,
                "created_at": str(datetime.now()),
            }
            results.append(data)
        return results
    else:
        data = {
            "prompt": prompts,
            "response": response,
            "created_at": str(datetime.now()),
        }
        return [data]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_file",
        type=str,
        help="The input file that contains the prompts to Mixtral-8x7B-Instruct.",
    )
    parser.add_argument(
        "--output_file",
        type=str,
        help="The output file to save the responses from Mixtral-8x7B-Instruct.",
    )
    parser.add_argument(
        "--engine",
        type=str,
        help="The MistralAI engine to use.",
    )
    parser.add_argument(
        "--max_tokens",
        default=500,
        type=int,
        help="The max_tokens parameter of Mixtral-8x7B-Instruct.",
    )
    parser.add_argument(
        "--temperature",
        default=0.7,
        type=float,
        help="The temprature of Mixtral-8x7B-Instruct.",
    )
    parser.add_argument(
        "--top_p",
        default=0.5,
        type=float,
        help="The `top_p` parameter of Mixtral-8x7B-Instruct.",
    )
    parser.add_argument(
        "--frequency_penalty",
        default=0,
        type=float,
        help="The `frequency_penalty` parameter of Mixtral-8x7B-Instruct.",
    )
    parser.add_argument(
        "--presence_penalty",
        default=0,
        type=float,
        help="The `presence_penalty` parameter of Mixtral-8x7B-Instruct.",
    )
    parser.add_argument(
        "--stop_sequences",
        default=["\n\n"],
        nargs="+",
        help="The `stop_sequences` parameter of Mixtral-8x7B-Instruct.",
    )
    parser.add_argument(
        "--logprobs",
        default=5,
        type=int,
        help="The `logprobs` parameter of Mixtral-8x7B-Instruct"
    )
    parser.add_argument(
        "--n",
        type=int,
        help="The `n` parameter of Mixtral-8x7B-Instruct. The number of responses to generate."
    )
    parser.add_argument(
        "--best_of",
        type=int,
        help="The `best_of` parameter of GPT3. The beam size on the Mixtral-8x7B-Instruct server."
    )
    parser.add_argument(
        "--use_existing_responses",
        action="store_true",
        help="Whether to use existing responses from the output file if it exists."
    )
    parser.add_argument(
        "--request_batch_size",
        default=20,
        type=int,
        help="The number of requests to send to Mixtral-8x7B-Instruct at a time."
    )
    return parser.parse_args()


if __name__ == "__main__":
    random.seed(123)
    args = parse_args()
    os.makedirs(os.path.dirname(args.output_file), exist_ok=True)

    # read existing file if it exists
    existing_responses = {}
    if os.path.exists(args.output_file) and args.use_existing_responses:
        with open(args.output_file, "r") as fin:
            for line in fin:
                data = json.loads(line)
                existing_responses[data["prompt"]] = data

    # do new prompts
    with open(args.input_file, "r") as fin:
        if args.input_file.endswith(".jsonl"):
            all_prompts = [json.loads(line)["prompt"] for line in fin]
        else:
            all_prompt = [line.strip().replace("\\n", "\n") for line in fin]

    with open(args.output_file, "w") as fout:
        for i in tqdm.tqdm(range(0, len(all_prompts), args.request_batch_size)):
            batch_prompts = all_prompts[i: i + args.request_batch_size]
            if all(p in existing_responses for p in batch_prompts):
                for p in batch_prompts:
                    fout.write(json.dumps(existing_responses[p]) + "\n")
            else:
                results = make_requests(
                    engine=args.engine,
                    prompts=batch_prompts,
                    max_tokens=args.max_tokens,
                    temperature=args.temperature,
                    top_p=args.top_p,
                    frequency_penalty=args.frequency_penalty,
                    presence_penalty=args.presence_penalty,
                    stop_sequences=args.stop_sequences,
                    logprobs=args.logprobs,
                    n=args.n,
                    best_of=args.best_of,
                )
                for data in results:
                    fout.write(json.dumps(data) + "\n")