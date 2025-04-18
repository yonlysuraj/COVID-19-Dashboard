# COVID-19 Dashboard India

An interactive dashboard built with Dash and Plotly to visualize COVID-19 cases across Indian states.

## Features

- Real-time visualization of COVID-19 statistics
- Interactive pie and bar charts showing state-wise distribution
- Filtering capability based on patient status (All/Hospitalized/Recovered/Deceased)
- Responsive design with Bootstrap integration

## Technologies Used

- Python 3.8+
- Dash
- Plotly
- Pandas
- NumPy
- Bootstrap 4

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/covid19-dashboard.git
cd covid19-dashboard
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Project Structure

```
COVID-19/
├── app.py              # Main dashboard application
├── dataset/
│   └── IndividualDetails.csv
│   └── covid_19_india.csv
│   └── AgeGroupDetails.csv
├── model/
│   └── operation.ipynb
├── requirements.txt
└── README.md
```

## Usage

1. Run the dashboard:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://127.0.0.1:8050/
```

## Dashboard Components

- **Summary Cards**: Display total cases, active cases, recoveries, and deaths
- **State-wise Distribution**: Interactive pie chart showing case distribution
- **Case Comparison**: Bar chart comparing cases across states
- **Status Filter**: Dropdown to filter data by patient status

## Data Source

The dashboard uses COVID-19 patient data from India, stored in `dataset/IndividualDetails.csv`.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Your Name - mail4suraj2002@gmail.com
Project Link: [https://github.com/yonlysuraj/covid19-dashboard](https://github.com/yonlysuraj/covid19-dashboard)