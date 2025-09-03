# COVID-19 Global Data Tracker

A data analysis and reporting notebook that tracks global COVID-19 trends.  It provides interactive maps, charts, and key statistics to help users understand the current state of the pandemic and its historical trends. The project analyzes cases, deaths, recoveries, and vaccinations across countries and time. 

## Objectives

This project aims to:
✅ Import and clean COVID-19 global data
✅ Analyze time trends (cases, deaths, vaccinations)
✅ Compare metrics across countries/regions
✅ Visualize trends with charts and maps
✅ Communicate findings in a Jupyter Notebook 


1️⃣ Data Collection
Obtain a reliable COVID-19 dataset from https://www.kaggle.com/datasets (cleaned CSV from Our World in Data)
Download owid-covid-data.csv from the above link.
Saved in my working folder.


### Data Loading & Exploration
Loaded the data using pandas.read_csv().
Checked columns: df.columns.
Previewed rows: df.head().
Identified missing values: df.isnull().sum()
Tools used: Pandas
key columns analyzed: date, location, total_cases, total_deaths, new_cases, new_deaths, total_vaccinations

### Data Cleaning
Filtered countries of interest (Kenya, USA, India).
Dropped rows with missing dates/critical values.
Converted date column to datetime: pd.to_datetime().
Handled missing numeric values with fillna() or interpolate().
✅ Tools: pandas

### Exploratory Data Analysis (EDA)
Plotted total cases over time for selected countries.
Plotted total deaths over time.
Compared daily new cases between countries.
Calculated the death rate: total_deaths / total_cases.
✅ Visualizations:
Line charts (cases & deaths over time).
Bar charts (top countries by total cases).
Heatmaps (optional for correlation analysis).
✅ Tools: matplotlib & seaborn

### Visualizing Vaccination Progress
Plotted cumulative vaccinations over time for selected countries.
Compared % vaccinated population.
✅ Charts: Line charts, Pie charts for vaccinated vs. unvaccinated.
✅ Tools: matplotlib & seaborn

## Tools and Libraries Used

*   **Programming Language:** Python & VS code with Jupyter extension
*   **Data Analysis & Manipulation:**
    *   Pandas
    *   NumPy
*   **Data Visualization:**
    *   [e.g., Matplotlib, Seaborn] 
*   **Data Sources:**
    *   [https://www.kaggle.com/datasets] [https://github.com/CSSEGISandData/COVID-19]

## How to Run/View the Project

1.  **Clone the repository:**

    ```bash
    git clone [your_repository_url]
    cd [your_project_directory]
    ```

2.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
    *(Make sure you have a `requirements.txt` file listing all the dependencies. If you don't have one, create it by running `pip freeze > requirements.txt` in your project environment.)*

3.  **Running the Application:**
    *   If you used flask, type this:
    ```bash
    python app.py
    ```
    *   If you used streamlit, type this:
    ```bash
    streamlit run app.py
    ```
    *(Replace `app.py` with the name of your main application file)*

4.  **Access the Application:**

    Open your web browser and go to [http://localhost:5000](http://localhost:5000) (or the appropriate address and port displayed in your terminal after running the application).
    *(Adjust the URL if your application runs on a different port or address.)*

## Insights and Reflections

*   **Data Challenges:** "Data inconsistencies between different sources required careful cleaning and merging strategies."
*   **Visualization Choices:** "Interactive maps were used to effectively illustrate the geographic spread of the virus, while line charts were used to show trends over time."
*   **Limitations:** "The project relies on publicly available data, which may have reporting delays or inaccuracies."
*   **Future Enhancements:** Future enhancements could include incorporating vaccination data, analyzing demographic factors, or implementing predictive models.
*   **Key Findings:** The analysis revealed a strong correlation between population density and infection rates in major cities.
*   [**Project insights:** The project highlights the importance of international collaboration in data sharing and pandemic response. The visualization demonstrates how quickly the virus can spread across borders, emphasizing the need for coordinated efforts to control outbreaks.]

## Project Structure
[your_project_directory]/ ├── README.md # This file ├── app.py # Main application file (or similar) ├── requirements.txt # List of dependencies ├── data/ # Directory for storing data files (if any) ├── notebooks/ # Directory for Jupyter notebooks (if any) ├── templates/ # Directory for HTML templates (if using Flask/Django) ├── static/ # Directory for CSS, JavaScript, and images (if any) └── ... # Other project-related files

*(Adjust the project structure to accurately reflect your project's organization)*

## Credits

*   [Salome Mundia]
*   [Mention any collaborators or contributors]
*   Data sources mentioned above.
