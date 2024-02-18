# Efficient Peak: Attention Loss Detection using Machine Learning

## Project Description

Efficient Peak is a project focused on detecting attention loss and loss of focus at work using machine learning methods. The project analyzes data such as mouse clicks, keyboard clicks, and screen saver activity to identify periods when the user may be losing interest or focusing on something else.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/efficient-peak.git
cd efficient-peak
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the program:

```bash
python efficient_peak.py
```

2. The program will start monitoring mouse activity, keyboard input, and screen saver activity.

3. The results of data processing will be displayed in the console or available in a report file.

## Configuration

In the `config.yml` file, you can configure various algorithm parameters and additional settings.

```yaml
# config.yml

algorithm:
  mouse_click_threshold: 5
  keyboard_click_threshold: 3
  screen_saver_threshold: 300

reporting:
  report_format: txt
  output_path: ./reports/efficient_peak_report.txt
```

## Data

The project utilizes data on mouse clicks, keyboard key presses, and screen saver activity for model training. Ensure the availability of a sufficient volume of diverse data for more accurate attention loss detection.

## License

This project is licensed under the terms of the MIT license - details can be found in the `LICENSE` file.

## Contributions and Feedback

We welcome your contributions! If you have suggestions or bug reports, please create an issue or submit a pull request.

Created with ❤️ by the Efficient Peak team.
