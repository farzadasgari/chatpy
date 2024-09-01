<div align="center">
   <h1>ChatPy</h1>
</div>

This is a simple chatbot created using Python and Natural Language Processing (NLP). The chatbot can handle basic conversations like greetings, farewells, and answering specific queries based on predefined intents.

## Project Structure

- `intents.json`: Contains the predefined intents, patterns, and responses for the chatbot.
- `app.py`: The main script that loads the intents, processes user input, and generates responses using NLP techniques. It also runs the GUI.
- `train.py`: A script to train the chatbot model using the data from `intents.json`.
- `model.py`: Contains the neural network model architecture used for predicting user intents.
- `nltk_utils.py`: Utility functions for text preprocessing, including tokenization and stemming.
- `chat.py`: Provides a command-line interface (CLI) for interacting with the trained chatbot, separate from the GUI.

## How It Works

1. **Load Data**: The chatbot loads the intents from the `intents.json` file.
2. **Process Input**: User input is processed using NLP techniques such as tokenization and stemming.
3. **Predict Intent**: Based on the processed input, the chatbot predicts the intent of the user using the trained model.
4. **Generate Response**: The chatbot selects an appropriate response from the predefined responses in the `intents.json` file.
5. **GUI Interaction**: The chatbot can be interacted with through a graphical user interface (GUI) built using Tkinter, providing a user-friendly experience.
<div align="center">
  <img src="https://github.com/farzadasgari/chatpy/blob/main/images/screen.PNG?raw=true">
</div>

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/farzadasgari/chatpy.git
   ```
2. Navigate to the project directory:
   ```bash
   cd chatpy
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Train the model:
   ```bash
   python train.py
   ```
5. Run the chatbot with GUI:
   ```bash
   python app.py
   ```

## Future Enhancements

- Implementing a more advanced NLP model for better intent recognition.
- Adding more intents and responses to make the chatbot more versatile.
- Integrating with external APIs to provide real-time data or services.
- Enhancing the GUI with more features and customization options.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/farzadasgari/chatpy/blob/main/LICENSE) file for details.

## Contact
For any inquiries, please contact:
- std_farzad.asgari@alumni.khu.ac.ir
- khufarzadasgari@gmail.com


## Links

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://farzadasgari.ir/)

[![Google Scholar Badge](https://img.shields.io/badge/Google%20Scholar-4285F4?logo=googlescholar&logoColor=fff&style=for-the-badge)](https://scholar.google.com/citations?user=Rhue_kkAAAAJ&hl=en)

[![ResearchGate Badge](https://img.shields.io/badge/ResearchGate-0CB?logo=researchgate&logoColor=fff&style=for-the-badge)](https://www.researchgate.net/profile/Farzad-Asgari)

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/farzad-asgari-5a90942b2/)
