//Form1.cs file for Windows forms app in Ms VS. Required: button, textBox.
namespace WinFormsApp2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string input = textBox1.Text;
            Stack<char> stack = new Stack<char>();
            int count = 1;
            int removedCount = 0;

            for (int i = 1; i < input.Length; i++)
            {
                if (input[i] == input[i - 1])
                {
                    count++;
                }
                else
                {
                    if (count < 3)
                    {
                        for (int j = 0; j < count; j++)
                        {
                            stack.Push(input[i - 1]);
                        }
                    }
                    else
                    {
                        removedCount += count;
                    }
                    count = 1; 
                }
            }

            if (count < 3)
            {
                for (int j = 0; j < count; j++)
                {
                    stack.Push(input[input.Length - 1]);
                }
            }
            else
            {
                removedCount += count; 
            }

            string result = new string(stack.ToArray());
            textBox1.Text = new string(result.Reverse().ToArray());
            MessageBox.Show($"Символов уничтожено: {removedCount}");
        }
    }
}
