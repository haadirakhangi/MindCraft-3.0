# MINDCRAFT

# Problem Statement
The traditional education system and current online learning platforms such as Udemy and Coursera present significant challenges for students worldwide, particularly for those from economically disadvantaged backgrounds or rural areas with limited access to qualified teachers and quality educational content. These platforms rely heavily on pre-existing courses created by professors or organizations, which can be costly, predominantly English-based, and often lack coverage of emerging or niche topics. Furthermore, the static nature of these platforms does not accommodate personalized learning needs or diverse learning styles, and the absence of multilingual support hinders comprehension for non-native speakers.

As a result, many students are unable to access or afford high-quality educational resources, which limits their learning opportunities and potential. Additionally, the rapid pace of advancements in various fields outstrips the ability of traditional platforms to provide up-to-date content, leaving students without timely resources for new topics. Generative AI, with its capability to produce dynamic and personalized educational content based on vast amounts of training data, offers a promising solution. However, even these models are restricted by the scope of their training data and cannot generate content on topics outside their knowledge base.

To address these issues, we have developed MindCraft, an AI-driven platform that aims to democratize education by generating on-demand, personalized, and multilingual courses across a wide range of subjects, making quality education accessible to all, regardless of economic or linguistic barriers.

# Project Setup Guide

This guide will walk you through the process of setting up your client project. Please follow the steps below:

## Prerequisites

- Node.js and npm installed on your machine.
- Python and pip installed on your machine.
- Virtualenv installed globally (`pip install virtualenv`).

## Steps

1. **Clone the Repository:**

    ```bash
    git clone <repository_url>
    ```

2. **Navigate to the Client Folder:**

    ```bash
    cd client
    ```

3. **Install Dependencies:**

    ```bash
    npm install
    ```

4. **Run the Client Development Server:**

    ```bash
    npm run dev
    ```

    This command starts the development server for the client application.

5. **Navigate to the Root Directory:**

    ```bash
    cd ..
    ```

6. **Set Up Virtual Environment:**

    ```bash
    virtualenv venv
    ```

7. **Activate Virtual Environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

8. **Install Python Dependencies:**

    ```bash
    pip install -r ./server/requirements.txt
    ```

9. **Create .env File:**

    Create a file named `.env` in the root directory and add the following content:

    ```plaintext
    GOOGLE_SERP_API_KEY = 'YOUR_GOOGLE_SERP_API_KEY'
    SERPER_API_KEY = 'YOUR_SERPER_API_KEY'
    TAVILY_API_KEY1 = 'YOUR_TAVILY_API_KEY1'
    TAVILY_API_KEY2 = 'YOUR_TAVILY_API_KEY2'
    TAVILY_API_KEY3 = 'YOUR_TAVILY_API_KEY3'
    GEMINI_API_KEY = 'YOUR_GEMINI_API_KEY'
    EMBEDDING_KEY = 'YOUR_GEMINI_API_KEY'
    SCRAPFLY_API_KEY = 'YOUR_SCRAPFLY_API_KEY'
    SECRET_KEY = 'YOUR_SECRET_KEY'
    ```

    Replace `YOUR_GOOGLE_SERP_API_KEY`, `YOUR_SERPER_API_KEY`, `YOUR_TAVILY_API_KEY1`, `YOUR_TAVILY_API_KEY2`, `YOUR_TAVILY_API_KEY3`, `YOUR_GEMINI_API_KEY`, `YOUR_GEMINI_API_KEY`, `YOUR_SCRAPFLY_API_KEY`, and `YOUR_SECRET_KEY` with your actual API keys and secret key.

10. **Run Flask Server:**

    ```bash
    python app.py
    ```

11. **Access Your Application:**


    Once the Flask server is running, you can access your application by visiting `http://localhost:5000` in your web browser.

    
    
![WhatsApp Image 2024-04-24 at 11 28 28 PM](https://github.com/Mehekjain05/MindCraft/assets/85340069/652d6648-4c39-47e8-b1e2-8929abf7334c)



![WhatsApp Image 2024-04-24 at 11 28 54 PM](https://github.com/Mehekjain05/MindCraft/assets/85340069/b48491bc-9aa1-4b84-8912-a30fd904ef24)



![WhatsApp Image 2024-04-24 at 11 32 15 PM](https://github.com/Mehekjain05/MindCraft/assets/85340069/6dea0ee7-5798-4353-a54f-b9398c4a5e13)



![WhatsApp Image 2024-04-24 at 11 31 32 PM](https://github.com/Mehekjain05/MindCraft/assets/85340069/3ea0ddd7-0bff-4e41-b144-89d74c8a6fc8)


![module_mr](https://github.com/user-attachments/assets/45fdc250-d96e-4668-8762-d529a32c5740)

