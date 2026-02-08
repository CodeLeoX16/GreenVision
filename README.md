<div align="center">

# 🌲 GreenVision - Forest Cover Type Prediction 🌲 

<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen" alt="Python"/>
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
<img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB"/>  

### *Predicting forest cover types using cartographic variables and machine learning*

[Dataset](https://www.kaggle.com/competitions/forest-cover-type-prediction/data) • [Docker Hub](https://hub.docker.com/r/codeleox1608/greenv)

</div>

---

## 📖 About The Project

We predict the forest cover type (the predominant kind of tree cover) from strictly cartographic variables (as opposed to remotely sensed data). The actual forest cover type for a given 30 x 30 meter cell was determined from US Forest Service (USFS) Region 2 Resource Information System data.

---

## <img src="https://c.tenor.com/NCRHhqkXrJYAAAAi/programmers-go-internet.gif" width="25"> Built With

- **Python** - Core programming language
- **FastAPI** - Modern web framework
- **Machine Learning** - Scikit-learn, XGBoost
- **Docker** - Containerization
- **MongoDB** - Database
- **AWS Services** - Cloud infrastructure

---

## 🐳 Quick Start with Docker (Recommended)

### Pull the Docker image
```bash
docker pull codeleox1608/greenv:latest
```

### Run the container
```bash
docker run -d -p 8080:8080 codeleox1608/greenv:latest
```

Then open your browser at `http://localhost:8080`

---

## 🛠️ Run Locally

### 1. Check if Dockerfile is available

### 2. Build the Docker image
```bash
docker build \
  --build-arg AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID> \
  --build-arg AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY> \
  --build-arg AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION> \
  --build-arg MONGODB_URL=<MONGODB_URL> \
  -t greenvision .
```

### 3. Run the Docker container
```bash
docker run -d -p 8080:8080 greenvision
```

---

## 💻 Development Setup

### Creating conda environment
```bash
conda create -p venv python==3.8 -y
```

### Activate conda environment
```bash
conda activate ./venv
```

### Install requirements
```bash
pip install -r requirements.txt
```

### Export environment variables
```bash
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
export AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION>
export MONGODB_URL="mongodb+srv://<username>:<password>@ineuron-ai-projects.7eh1w4s.mongodb.net/?retryWrites=true&w=majority"
```

### Run the server
```bash
python app.py
```

### Launch UI
Open your browser at: `http://127.0.0.1:5000/`

---

## 🌐 Infrastructure & Technologies

### Cloud Infrastructure
- **AWS S3** - Storage
- **AWS EC2** - Compute
- **AWS ECR** - Container Registry
- **GitHub Actions** - CI/CD
- **Terraform** - Infrastructure as Code

---

## <img src="https://media2.giphy.com/media/QssGEmpkyEOhBCb7e1/giphy.gif?cid=ecf05e47a0n3gi1bfqntqmob8g9aid1oyj2wr3ds3mg700bl&rid=giphy.gif" width="25"> Project Snippets

### FlowChart
<img src="snippets/flowchart.png" alt="FlowChart" width="800"/>

### Application Screenshots
<div align="center">
<img src="snippets/snip1.png" alt="Screenshot 1" width="400"/>
<img src="snippets/snip2.png" alt="Screenshot 2" width="400"/>
<img src="snippets/snip3.png" alt="Screenshot 3" width="400"/>
<img src="snippets/snip4.png" alt="Screenshot 4" width="400"/>
<img src="snippets/snip5.png" alt="Screenshot 5" width="400"/>
</div>

---

## <img src="https://media.giphy.com/media/iY8CRBdQXODJSCERIr/giphy.gif" width="25"> Data Understanding

The dataset used is from Kaggle's Forest Cover Type Prediction competition:

- **581,012** samples (rows)
- **55** features (columns) 
- **1** target column (Cover_Type)
- **7** different forest cover types

The features are strictly cartographic variables including:
- Elevation
- Aspect
- Slope
- Distances to water, roads, and fire points
- Wilderness area designations
- Soil type classifications

---

## 🏭 Industrial Use Cases

1. **Wildfire Prevention** - Scientists can predict future wild fires and protect flora and fauna
2. **Fire Rating Systems** - Develop comprehensive fire risk assessment tools
3. **Forest Management** - Optimize resource allocation for forest preservation
4. **Environmental Planning** - Support decision-making for land use and conservation

---

## <img src="https://media2.giphy.com/media/QssGEmpkyEOhBCb7e1/giphy.gif?cid=ecf05e47a0n3gi1bfqntqmob8g9aid1oyj2wr3ds3mg700bl&rid=giphy.gif" width="25"> Tech Stack & Libraries

<div align="center">

### Core Technologies
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen" alt="Python"/>
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
<img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB"/>

### Data Science & ML
<img src="https://matplotlib.org/_static/logo2_compressed.svg" alt="Matplotlib" height="40"/>
<img src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" alt="Seaborn" height="40"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/768px-Pandas_logo.svg.png" alt="Pandas" height="40"/>
<img src="https://www.vectorlogo.zone/logos/numpy/numpy-ar21.svg" alt="NumPy" height="40"/>
<img src="https://raw.githubusercontent.com/valohai/ml-logos/master/scipy.svg" alt="SciPy" height="40"/>
<img src="https://seeklogo.com/images/S/scikit-learn-logo-8766D07E2E-seeklogo.com.png" alt="Scikit-learn" height="40"/>

### Development Tools
<img src="https://upload.wikimedia.org/wikipedia/commons/7/7e/Spyder_logo.svg" alt="Spyder" height="40"/>
<img src="https://www.vectorlogo.zone/logos/jupyter/jupyter-ar21.svg" alt="Jupyter" height="40"/>

</div>

---

<div align="center">

### 🌟 Star this repository if you find it helpful! 🌟

**Made with ❤️ by [CodeLeoX16](https://github.com/CodeLeoX16)**

</div>
