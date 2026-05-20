from openai import OpenAI


def call_openai_api() -> str:
    client = OpenAI()

    response = client.responses.create(
        model="gpt-5.5",
        input="Write a one-sentence bedtime story about a unicorn.",
    )

    return response.output_text


def main() -> None:
    print(call_openai_api())


if __name__ == "__main__":
    main()
