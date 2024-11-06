using System;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        // Пункты из 2.3:
        private void добавитьToolStripMenuItem_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Добавляем...");
        }
        private void удалитьToolStripMenuItem_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Удаляем!!");
        }
        private void переместитьToolStripMenuItem_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Перемещаем...");
        }
        private void уведомитьToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }
        private void сообщение1ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            ToolStripMenuItem item = (ToolStripMenuItem)sender;
            string message = item.Text;
            MessageBox.Show(message);
        }
        // Стиль бегунка, клики:
        private void menuItemNone_Click(object sender, EventArgs e)
        {
            trackBar1.TickStyle = TickStyle.None;
        }
        private void menuItemTopLeft_Click(object sender, EventArgs e)
        {
            trackBar1.TickStyle = TickStyle.TopLeft;
        }
        private void menuItemBottomRight_Click(object sender, EventArgs e)
        {
            trackBar1.TickStyle = TickStyle.BottomRight;
        }
        private void menuItemBoth_Click(object sender, EventArgs e)
        {
            trackBar1.TickStyle = TickStyle.Both;
        }
        // Трекбар ориентация
        private void вертикальнаяToolStripMenuItem_Click(object sender, EventArgs e)
        {
            trackBar1.Orientation = Orientation.Vertical;
        }
        private void горизонтальнаяToolStripMenuItem_Click(object sender, EventArgs e)
        {
            trackBar1.Orientation = Orientation.Horizontal;
        }
        // Мусор, случайно нажал:
        private void командаМенюToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }
        private void menuStrip1_ItemClicked(object sender, ToolStripItemClickedEventArgs e)
        {

        }

        private void ориентацияToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }
    }
}
