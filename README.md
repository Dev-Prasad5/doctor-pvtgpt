# Doctor GPT

This is an interactive Doctor GPT model that allows users to ask about doctors specializing in various fields of medicine, such as cardiology, dermatology, and more. The model has been fine-tuned on data scraped from a medical website, enabling it to provide responses based on user queries related to doctor specialties.

## Steps to Use:

1. **Install Dependencies:**

   ```bash
   !pip install -r requirements.txt


2. **Clone the Repository:**

   ```bash
   !git clone https://github.com/Dev-Prasad5/doctor-pvtgpt.git
   %cd /content/doctor-pvtgpt
   ```

3. **Run the Inference Script:**
   ```bash
   !python data_doct.py
   ```

   ```bash
   !python train_model.py
   ```

   ```bash
   !python test_interact.py
   ```
   This will launch a Streamlit app where you can interact with the model.

4. **Optional**: You can deploy this app in Google Colab or a local machine for testing.

## Notes:
- The model can answer questions like "Who treats heart?", "Who specializes in plastic surgery?", and so on.

## Model Functionality

- The fine-tuned model can respond to queries such as:

    - "Who treats heart problems?"
    - "Who specializes in plastic surgery?"
    - "Who is a cardiologist?"

The model answers by listing doctors who specialize in the requested field based on the scraped data.

## Data Scraping
 * Website Used:
      [Medindia - Doctor Appointment]([https://website-name.com](https://www.medindia.net/doctor-appointment/tele-consultation.asp?category=Allopathy%20Doctors))

 - The doctor profiles were scraped from Medindia - Doctor Appointment. The data collected includes:
    - Doctor Names
    - Specialties
- The data was scraped using Selenium and stored in doctors_data.json.

## Data Preprocessing & Model Training
 * Data Preparation:
The raw data was processed and structured into a text-based format for model training. Each entry consists of the Doctor's Name and Specialty.
* Fine-tuning the Model:
A pre-trained GPT-2 model from the Hugging Face Transformers library was fine-tuned on the processed data. The model was trained on these doctor names and specialties to generate relevant responses to user queries.
* After training, the model was saved and integrated into a Streamlit web app for easy interaction.

## Output Sample:
![test_interact](https://github.com/user-attachments/assets/d9fb45e1-5dcd-48a6-b04f-4c180376612f)

## Conclusion
* This project demonstrates how to scrape data from medical websites, preprocess it, fine-tune a GPT-2 model, and integrate it into an interactive web app. The Doctor GPT model allows users to easily query doctor specialties and get relevant responses, providing a valuable tool for anyone looking to connect with healthcare professionals.

