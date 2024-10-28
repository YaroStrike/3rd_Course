using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Windows.Forms.DataVisualization.Charting;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            //string currentDirectory = Environment.CurrentDirectory;
            //MessageBox.Show($"Папка: {currentDirectory}");
            InitializeComponent();
            string imagePath = "input.png"; 
            pictureBox1.Image = Image.FromFile(imagePath);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            double a = 0.1;
            double b = 1.0;
            double xStart = -4.0;
            double xEnd = -6.2;
            double dx = -0.2;

            DataTable dataTable = new DataTable();
            dataTable.Columns.Add("x");
            dataTable.Columns.Add("y");
            dataTable.Columns.Add("y'");

            chart1.Series.Clear();
            Series seriesFunction = new Series("Функция");
            Series seriesDerivative = new Series("Производная");

            for (double x = xStart; x >= xEnd; x += dx)
            {
                double y = x + Math.Sqrt(Math.Abs(Math.Pow(x, 3) + a - b * Math.Exp(x)));
                double derivative = 1 + (3 * Math.Pow(x, 2) / (2 * Math.Sqrt(Math.Abs(Math.Pow(x, 3) + a - b * Math.Exp(x)))));

                dataTable.Rows.Add(x, y, derivative);
                seriesFunction.Points.AddXY(x, y);
                seriesDerivative.Points.AddXY(x, derivative);
            }

            chart1.Series.Add(seriesFunction);
            chart1.Series.Add(seriesDerivative);
            chart1.ChartAreas[0].AxisX.Title = "x";
            chart1.ChartAreas[0].AxisY.Title = "y";

            dataGridView1.DataSource = dataTable;
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }
    }
}
