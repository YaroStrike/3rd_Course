using Microsoft.VisualStudio.TestTools.UnitTesting;

[TestClass]
public class testing
{
    [TestMethod]
    public void TestArithmeticOperations()
    {
        double num1 = 10;
        double num2 = 5;

        double expectedSum = 15;
        double expectedDifference = 5;
        double expectedProduct = 50;
        double expectedQuotient = 2;

        Assert.AreEqual(expectedSum, num1 + num2);
        Assert.AreEqual(expectedDifference, num1 - num2);
        Assert.AreEqual(expectedProduct, num1 * num2);
        Assert.AreEqual(expectedQuotient, num1 / num2);
    }
}
