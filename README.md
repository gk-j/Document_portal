## Conda environment setup
    ```
    conda create -p venv python==3.12 -y

    conda activate ./venv/

    ```

## Project setup

    ```
    git clone https://github.com/gk-j/Document_portal

    cd Document_portal

    code .

    # Create a new Conda environment with Python 3.10
    conda create -p <env_name> python=3.10 -y

    # Activate the environment (use full path to the environment)
    conda activate <path_of_the_env>

    # Install dependencies from requirements.txt
    pip install -r requirements.txt
    ```

## project requirements
1.LLM_Model 
        groq(free)
        openai(paid)
        gemini(paid)
        claude(paid)
        huggingface(free)
        ollama(local setup)

2.embedding model ##openai,huggingface,gemini

3.vector database ##inmemory,ondisk,cloudbased
