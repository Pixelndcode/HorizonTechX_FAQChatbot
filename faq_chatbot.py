print("=== AI-Based FAQ Chatbot ===")

faq = {
    "what is ai": "AI stands for Artificial Intelligence. It enables machines to perform tasks that normally require human intelligence.",

    "what is machine learning": "Machine Learning is a branch of AI that allows systems to learn from data and improve automatically.",

    "what is deep learning": "Deep Learning is a subset of Machine Learning that uses neural networks with multiple layers.",

    "what is nlp": "NLP stands for Natural Language Processing. It helps computers understand and process human language.",

    "what is data science": "Data Science involves collecting, analyzing, and interpreting data to gain useful insights.",

    "what is python": "Python is a popular programming language widely used in AI, Machine Learning, and Data Science.",

    "what is a chatbot": "A chatbot is a software program that can interact with users through text or voice conversations.",

    "what is chatgpt": "ChatGPT is an AI language model developed by OpenAI that can answer questions and generate text.",

    "what is computer vision": "Computer Vision is a field of AI that enables computers to understand and analyze images and videos.",

    "what is artificial intelligence": "Artificial Intelligence is the simulation of human intelligence in machines."
}

while True:
    question = input("\nAsk a Question (type 'exit' to quit): ").lower()

    if question == "exit":
        print("Thank you for using the AI FAQ Chatbot!")
        break

    if question in faq:
        print("Bot:", faq[question])
    else:
        print("Bot: Sorry, I don't have an answer to that question.")