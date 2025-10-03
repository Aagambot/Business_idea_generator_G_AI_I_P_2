# IdeaGen: A Full-Stack AI-Powered SaaS Application

IdeaGen is a complete full-stack SaaS application that generates innovative business ideas using AI. This project demonstrates how to build a scalable and secure application with a modern tech stack, including a Next.js frontend, a Python FastAPI backend, and Clerk for authentication and billing.

## ✨ Features

  - **AI-Powered Generation**: Generates business ideas tailored for the AI agent economy using a large language model.
  - **Real-Time Streaming**: Streams AI responses to the frontend in real time for an engaging user experience.
  - **Full-Stack Architecture**: Combines a Next.js (Pages Router) frontend with a FastAPI Python backend on Vercel.
  - **User Authentication**: Securely authenticates users with Clerk, supporting multiple providers like Google, GitHub, and email.
  - **Subscription Management**: Integrates Clerk Billing to gate premium content, handle payments, and manage subscriptions.
  - **Professional UI/UX**: Features a modern, responsive design with Tailwind CSS and a professional, glassmorphism-inspired aesthetic.
  - **Production-Ready**: Seamlessly deploys to Vercel, which handles both the Next.js frontend and the Python backend as serverless functions.

-----

## 🛠️ Tech Stack

### Frontend

  - **Next.js**: The React framework for building fast and scalable web applications.
  - **TypeScript**: Ensures type safety throughout the codebase.
  - **Tailwind CSS**: A utility-first CSS framework for rapid UI development.
  - **`react-markdown`**: Renders beautifully formatted Markdown content from the AI response.
  - **`@clerk/nextjs`**: The SDK for integrating Clerk's authentication and user management into the Next.js app.
  - **`@microsoft/fetch-event-source`**: Handles Server-Sent Events (SSE) for real-time streaming with authentication headers.

### Backend

  - **FastAPI**: A modern, fast (high-performance) Python web framework for building APIs.
  - **`uvicorn`**: An ASGI server for running the FastAPI application.
  - **GOOGLE API**: The core AI engine for generating business ideas.
  - **`fastapi-clerk-auth`**: A library to securely verify JWT tokens from Clerk.

### Deployment & Tools

  - **Vercel**: The all-in-one platform for deploying the Next.js frontend and the FastAPI backend as serverless functions.
  - **Clerk**: The authentication and billing platform that provides user sign-in, sign-up, and subscription management.
  - **Vercel CLI**: For managing local development, linking, and deploying the project.

-----

## 🚀 Getting Started

Follow these steps to get a copy of the project up and running on your local machine and deployed to production.

### Prerequisites

  - Node.js installed on your machine.
  - Python 3.8+ installed on your machine.
  - Vercel CLI installed (`npm i -g vercel`).
  - An Google API key.
  - A Clerk account.

### Installation

1.  **Clone the repository:**

    ```bash
    git clone [repository_url]
    cd [your_project_directory]
    ```

2.  **Create the Next.js project:**

    ```bash
    npx create-next-app@latest saas --typescript
    ```

      - Choose **Yes** for ESLint and Tailwind CSS.
      - Choose **No** for `src/` directory, App Router, and Turbopack.

3.  **Install frontend dependencies:**

    ```bash
    npm install @clerk/nextjs @microsoft/fetch-event-source react-markdown remark-gfm remark-breaks @tailwindcss/typography
    ```

4.  **Create the Python backend:**

      - Create a new folder named `api` in the root directory.
      - Create a `requirements.txt` file in the root with the following content:
        ```
        fastapi
        uvicorn
        google-genai
        fastapi-clerk-auth
        ```
      - Create an `index.py` file inside the `api` folder and populate it with the FastAPI code from the project source.

5.  **Configure Environment Variables:**

      - Create a `.env.local` file in your project root.
      - Add your API keys from OpenAI and Clerk.
      - Get your JWKS URL from your Clerk dashboard under **API Keys**.

    <!-- end list -->

    ```bash
    GOOGLE_API_KEY=your_google_api_key_here
    NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=your_publishable_key_here
    CLERK_SECRET_KEY=your_secret_key_here
    CLERK_JWKS_URL=your_jwks_url_here
    ```

      - Add `.env.local` to your `.gitignore` file.

### Local Development

1.  **Run the project:**
    ```bash
    vercel dev
    ```
2.  **Access the application:**
      - Visit `http://localhost:3000` to see the landing page.
      - You can test the authentication flow locally, but note that the Python backend streaming will only work after deployment.

### Deployment

1.  **Link your project to Vercel:**

    ```bash
    vercel link
    ```

      - Follow the prompts to set up a new Vercel project.

2.  **Add environment variables to Vercel:**

    ```bash
    vercel env add GOOGLE_API_KEY
    vercel env add NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY
    vercel env add CLERK_SECRET_KEY
    vercel env add CLERK_JWKS_URL
    ```

      - Paste the respective keys when prompted and select **all environments**.

3.  **Deploy the application:**

    ```bash
    vercel --prod
    ```

      - This will build and deploy your application to a production URL.

-----

## 📚 Learnings

This project provides a comprehensive learning experience in building a modern full-stack application, covering key concepts such as:

  - Structuring a full-stack application with a Next.js frontend and a Python backend.
  - Implementing secure user authentication with JWT verification.
  - Handling real-time data streaming using Server-Sent Events (SSE).
  - Setting up subscription-based access and payment processing.
  - Deploying a complex, multi-language stack on a single platform like Vercel.

-----
