using System;

namespace WinFormsApp1
{
    public partial class Form1 : Form
    {
        private int score = 0;
        private int dropSpeed = 5;
        private System.Windows.Forms.Timer dropTimer;
        private Random random;

        public Form1()
        {
            InitializeComponent();
            random = new Random();
            dropTimer = new System.Windows.Forms.Timer();
            dropTimer.Interval = 100; // Adjust for speed
            LoadNewQuestion(); // Load a question to initialize IsCorrectAnswer
            dropTimer.Start();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            // Logic for moving raindrop and checking for user input
            // If raindrop reaches bottom, check answer
            // Update score and difficulty accordingly
        }

        private string? IsCorrectAnswer { get; set; }

        private void LoadNewQuestion()
        {
            string question = "What is 2 + 2?";
            IsCorrectAnswer = "4";
        }

        private void CheckAnswer(string userInput)
        {
            if (userInput.Equals(IsCorrectAnswer, StringComparison.OrdinalIgnoreCase))
            {
                score++;
                IncreaseDifficulty();
                IsCorrectAnswer = null;
            }
            else
            {
                score--;
                LoadNewQuestion();
            }
        }

        private void IncreaseDifficulty()
        {
            dropSpeed += 2; // Increase speed
            dropTimer.Interval = Math.Max(50, dropTimer.Interval - 10); // Decrease interval
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }
        private void textBox1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                string userInput = textBox1.Text;
                CheckAnswer(userInput);
                textBox1.Clear(); // Clear the TextBox for reuse
                e.SuppressKeyPress = true; // Prevent the 'ding' sound on Enter
            }
        }
    }
}
