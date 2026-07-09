# Learning_GenerativeAI_langchain

# Learning Generative AI with LangChain

This repository documents my journey learning Generative AI and LangChain — starting from basic prompt templates all the way to RAG (Retrieval-Augmented Generation) components. Built using open-source models via Hugging Face, with some local model experimentation as well.

## 📁 Project Structure & Topics Covered

### 1. Prompts (`models/1.LLMs`, `prompts/`)
- Basic `PromptTemplate` usage — building reusable prompts with placeholder variables
- Dynamic prompt generation with `from_template()` vs. the more explicit constructor-based approach
- Role-based prompts using `ChatPromptTemplate` and `MessagesPlaceholder`
- Saving and loading prompt templates to/from JSON (`template.save()` / `load_prompt()`)
- A Streamlit-based "Research Tool" UI for generating paper summaries with configurable style and length

### 2. Chat Models (`models/2.ChatModels`)
- Difference between base LLMs (plain text completion) and Chat Models (role-based, instruction-tuned)
- Working with Hugging Face models both via:
  - **`HuggingFaceEndpoint`** — free, API-hosted inference (used `Qwen/Qwen2.5-7B-Instruct`)
  - **`HuggingFacePipeline`** — running models locally (used `TinyLlama/TinyLlama-1.1B-Chat-v1.0`)
- Building a simple command-line chatbot with multi-turn conversation history

### 3. Embedding Models (`models/3.EmbeddedModels`)
- Generating text embeddings using `HuggingFaceEmbeddings` (local, free)
- Document similarity comparison
- (Explored OpenAI embeddings as well, though this requires a paid API key)

### 4. Structured Output (`outputs/`)
- Using **Pydantic** (`BaseModel`, `Field`) to define and validate structured data
- Type coercion, optional fields, and field constraints (`gt`, `lt`, `EmailStr`)
- Getting structured output from LLMs via:
  - `with_structured_output()` (found to be unsupported for this model/provider combination)
  - Manually prompting for JSON and validating the response against a Pydantic schema as a reliable workaround

### 5. Output Parsers (`output_parser/`)
- **`StrOutputParser`** — extracting plain string output from a model's response
- **`JsonOutputParser`** — asking the model to return valid JSON
- **`PydanticOutputParser`** — validating model output against a Pydantic class (modern replacement for the now-removed `StructuredOutputParser` / `ResponseSchema`)
- Notes on model reliability — smaller/less capable models often struggle to follow strict structured-output instructions consistently

### 6. Chains (`chains/`)
- **Sequential chains** — piping one model's output into the next step using LCEL (`|` operator)
- **Parallel chains** — running multiple chains simultaneously with `RunnableParallel` (e.g., generating notes and quiz questions from the same text, then merging them)
- **Conditional chains** — routing logic with `RunnableBranch` and `RunnableLambda` (e.g., classifying feedback sentiment, then responding differently based on the result)

### 7. RAG — Document Loaders (`RAG/Doc_loader`)
- **`TextLoader`** — loading plain text files
- **`DirectoryLoader`** + **`PyPDFLoader`** — loading multiple PDFs from a folder
- **`WebBaseLoader`** — scraping and loading content directly from a webpage URL

### 8. RAG — Text Splitters (`RAG/text_splitter`)
- **`CharacterTextSplitter`** — splitting text into fixed-size chunks
- **`SemanticChunker`** — splitting text based on semantic meaning/similarity rather than fixed character counts, using free Hugging Face embeddings (`sentence-transformers/all-MiniLM-L6-v2`) instead of paid OpenAI embeddings

### 9. Runnables (`runnable/`)
- Exploring LangChain's core `Runnable` interface and `RunnableSequence` for composing steps

## 🛠️ Setup

```bash
# Clone the repo
git clone https://github.com/shivamtharejavinove/Learning_GenerativeAI_langchain.git
cd Learning_GenerativeAI_langchain

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

Create a `.env` file in the project root with your API credentials:
```
HUGGINGFACEHUB_ACCESS_TOKEN=your_huggingface_token_here
```

Get a free Hugging Face token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).

## 📌 Key Learnings & Notes

- Free-tier Hugging Face inference has inconsistent model support — not every model on the Hub is available through the router API; some experimentation is needed to find models that work reliably (e.g., `Qwen/Qwen2.5-7B-Instruct` worked well; `google/gemma-2-2b-it` and `meta-llama/Llama-3.2-3B-Instruct` did not, at time of writing).
- Local models (via `HuggingFacePipeline`) work without an internet connection or rate limits but are significantly slower on CPU, especially for longer generations.
- Structured output (JSON/Pydantic schemas) is not equally well-supported across all models/providers — smaller models sometimes ignore formatting instructions and produce code or prose instead of the requested format.
- `langchain_community` is being deprecated in favor of smaller, standalone integration packages — expect import paths to keep shifting as the library evolves.

## 🚧 Status

This is an active learning project — new topics and experiments are added as I progress through the LangChain curriculum.
