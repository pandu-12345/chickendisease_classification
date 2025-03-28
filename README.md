
# Chicken Disease Classification

## 📌 **Project Overview**
Chicken Disease Classification is a deep learning-based project aimed at accurately identifying diseases in chickens through image classification. Early and precise detection of poultry diseases is crucial for maintaining the health of chickens and preventing the spread of infections, ultimately improving poultry farm productivity.

## 🚀 **Objective**
- To build a robust model that classifies chicken diseases using image data.
- To assist poultry farmers in early detection and treatment of diseases.

## 🏗️ **Dataset**
- The dataset consists of images of chickens exhibiting symptoms of various diseases.
- Classes include: **Healthy, Coccidiosis**.

## 🛠️ **Technologies Used**
- **Python** for programming.
- **TensorFlow** for deep learning.
- **VGG16** as the base model for transfer learning.
- **Docker** for containerization.
- **Apache Airflow** for orchestrating the ML pipeline.

## 🔍 **Model Architecture**
- VGG16 model with additional custom layers for classification.
- Performance metrics: **Accuracy**.

## ⚙️ **Workflow**
1. **Data Collection & Preprocessing**
2. **Model Training & Validation**
3. **Hyperparameter Tuning**
4. **Model Evaluation**
5. **Deployment using Docker**

## 📊 **Results**
- Achieved **86%** accuracy on the test set.
- Effective in early disease detection with high precision and recall.

## 🚢 **Deployment**
- Containerized using **Docker**.

## 🤝 **How to Use**
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/username/chicken-disease-classification.git
   ```
2. **Navigate to the Project Directory:**
   ```bash
   cd chicken-disease-classification
   ```
3. **Create Enviroment:**
    ```bash 
    conda create -n myenv python=3.10 -y
    ```
4. **Activate Enviroment:**
   ```bash
   conda activate myenv
   ```
5. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```
6. **Run DVC repro:**
   ```bash
   dvc repro
   Python app.py
   ```
7. **Now**
   - Open `http://localhost:5000` in your browser.

## 🏅 **Future Enhancements**
- Increase dataset size for better generalization.
- Implement transfer learning with Vision Transformers (ViT).
- Real-time disease detection through edge devices.

## 📬 **Contributions**
Contributions are welcome! Feel free to raise issues or create pull requests.

## 📞 **Contact**
- **Name:** sudarshan kumar jha 
- **Email:** jhasudarshan8@gmail.com 



## Developer Workflow

1. update config.yaml
2. update secrets.yaml [optional]
3. update parameters.yaml 
4. update the entity
5. update the configuration manager in src config
6. update the components
7. update the pipline
8. update main.py
9. update the dvc.yaml