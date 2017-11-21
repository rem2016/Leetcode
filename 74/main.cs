public class Solution
{
    public delegate int del(int index);
    public int locate(del indexer, int l, int r, int target)
    {
        while (l != r)
        {
            int m = (l + r) / 2;
            int value = indexer(m);
            if (value == target)
            {
                return m;
            }
            if (value < target)
            {
                if (l == m)
                {
                    return l;
                }
                l = m;
            }
            else
            {
                r = m;
            }
        }
        return l;
    }
    public bool SearchMatrix(int[,] matrix, int target)
    {
        int n = matrix.GetLength(0), m = matrix.GetLength(1);
        if (m == 0 || n == 0)
            return false;
        del indexer = i => matrix[i, 0];
        int row = locate(indexer, 0, n, target);
        indexer = i => matrix[row, i];
        int col = locate(indexer, 0, m, target);
        Console.WriteLine(row);
        Console.WriteLine(col);
        return matrix[row, col] == target;
    }
}
