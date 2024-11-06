using System;
using System.Drawing;
using System.IO;
using System.Windows.Forms;

namespace WindowsFormsApp2
{
    public partial class Form1 : Form
    {
        private Random random = new Random();

        public Form1()
        {
            InitializeComponent();
            string imagePath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "star.png");
            pictureBoxStar.Image = Image.FromFile(imagePath);
            timerMovement.Interval = 100; // Интервал обновления в миллисекундах
            timerMovement.Tick += Timer_Tick;
            timerMovement.Start();
        }

        private void Timer_Tick(object sender, EventArgs e)
        {
            int x = random.Next(0, ClientSize.Width - pictureBoxStar.Width);
            int y = random.Next(0, this.ClientSize.Height - pictureBoxStar.Height);
            pictureBoxStar.Location = new Point(x, y);
        }
    }
}