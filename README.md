# Voice-Enabled Assistant

Welcome to the Voice-Enabled Assistant project – an intelligent, voice-activated virtual assistant designed to enhance user interactions through advanced speech recognition and natural language understanding. This project integrates OpenAI's Whisper for accurate voice processing, GPT-3.5-turbo for conversational intelligence, Microsoft Bing AI for additional context, and Amazon Polly for lifelike voice synthesis.

![Voice-Enabled Assistant](path/to/assistant-image.png)

## Key Features

- **Wake-Up Command Recognition:** Initiate conversations effortlessly with a personalized wake-up command, creating a seamless and engaging user experience.

- **Voice Input Processing:** Leverage OpenAI Whisper to transcribe voice input into text, enabling clear and accurate communication with the assistant.

- **Response Generation:** Utilize the power of GPT-3.5-turbo or Microsoft Bing AI to generate context-aware, informative responses tailored to user queries.

- **Voice Output Generation:** Transform text responses into expressive voice output using Amazon Polly, delivering a natural and human-like interaction.

## Getting Started

### Prerequisites

Before getting started, ensure you have the following:

- OpenAI Whisper API Key
- OpenAI GPT-3.5-turbo API Key
- Microsoft Bing AI API Key
- Amazon Polly API Key

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/voice-enabled-assistant.git
    cd voice-enabled-assistant
    ```

2. Install dependencies:

    ```bash
    npm install
    ```

3. Set up configuration:

    Copy the `.env.example` file to `.env` and add your API keys:

    ```env
    WHISPER_API_KEY=your-whisper-api-key
    CHATGPT_API_KEY=your-chatgpt-api-key
    BING_AI_API_KEY=your-bing-ai-api-key
    AMAZON_POLLY_API_KEY=your-amazon-polly-api-key
    ```

### Usage

1. Run the assistant:

    ```bash
    python assistant.py
    ```

2. Use the wake-up command and start a conversation with the assistant.

### Customization

If desired, you can customize the wake word or adjust other settings in the configuration files.

## Contribution

Contributions are welcome! Please follow the [contributing guidelines](CONTRIBUTING.md) to report issues, suggest improvements, or submit pull requests.

## License

This project is licensed under the MIT License, providing flexibility for integration and innovation.

## Acknowledgments

We extend our gratitude to the incredible technologies that form the backbone of this project, including OpenAI's Whisper and GPT-3.5-turbo, Microsoft Bing AI, and Amazon Polly.

Explore the endless possibilities of voice-enabled interactions with the Voice-Enabled Assistant project. Let your creativity and curiosity guide you as you dive into the world of voice-activated intelligence!
