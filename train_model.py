#train data for model
import json

# Load your scraped data (make sure you've saved it as cleaned_doctors_data.json)
with open('doctors_data.json', 'r', encoding='utf-8') as f:
    doctors_data = json.load(f)

# Prepare the training data (each entry will be a "Doctor: <name>, Specialty: <specialty>")
training_data = []
for doctor in doctors_data:
    training_data.append(f"Doctor: {doctor['name']}, Specialty: {doctor['specialty']}")

# Save the training data as a text file
with open('training_data.txt', 'w', encoding='utf-8') as f:
    for entry in training_data:
        f.write(entry + '\n')


##################################################################
#train modelusing data
from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments
from datasets import Dataset
import json

# Load the dataset (assuming it's a JSON file with a 'name' and 'specialty' field)
with open('doctors_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract the text for fine-tuning (combine name and specialty as an example)
texts = [f"{doctor['name']} - {doctor['specialty']}" for doctor in data]

# Convert to Hugging Face dataset format
train_dataset = Dataset.from_dict({"text": texts})

# Load GPT-2 model and tokenizer
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Set pad_token to eos_token (this resolves the padding issue)
tokenizer.pad_token = tokenizer.eos_token  # Use eos_token as pad_token

# Tokenize the dataset
def tokenize_function(examples):
    # Tokenize the input text
    tokenized_inputs = tokenizer(examples["text"], padding="max_length", truncation=True, max_length=512)

    # For language modeling, the labels are the same as the input text
    tokenized_inputs["labels"] = tokenized_inputs["input_ids"]

    return tokenized_inputs

tokenized_datasets = train_dataset.map(tokenize_function, batched=True)

# Training arguments
training_args = TrainingArguments(
    output_dir="./results",          # Where to save model checkpoints
    overwrite_output_dir=True,       # Whether to overwrite the output directory
    num_train_epochs=1,              # Number of training epochs
    per_device_train_batch_size=2,   # Batch size for training
    save_steps=10_000,               # Save checkpoints every 10,000 steps
    save_total_limit=2,              # Keep only the last 2 checkpoints
    logging_dir="./logs",            # Where to save logs
)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets,
)

# Fine-tune the model
trainer.train()

# Save the fine-tuned model
trainer.save_model("./fine_tuned_gpt2")
tokenizer.save_pretrained("./fine_tuned_gpt2")
