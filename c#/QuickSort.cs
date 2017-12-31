using System; 

namespace QuickSortAlgorythm
{
    class Program
    {       
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the Size of Array");
            int size = int.Parse(Console.ReadLine());  //Read array size.
            Console.WriteLine("Enter the Array elements");

            string[] usrInput = Console.ReadLine().Split(' '); //Read user input.

            int[] inputArray = new int[size];

            for (int i = 0; i < size; i++)
            {
                inputArray[i] = int.Parse(usrInput[i]); //Assign user input to array.
            }

            QuickSort(inputArray, 0, size - 1);

            Console.WriteLine("The sorted array after applying Quick Sort ");

            for (int k = 0; k < inputArray.Length; k++)
            {
                Console.Write(inputArray[k] + " "); //Print the sorted array to console.
            }
            Console.ReadLine();
        }

        static void QuickSort(int[] arr, int start, int end)
        {
            if (start < end)
            {
                //stores the position of pivot element
                int piv_pos = partition(arr, start, end);
                QuickSort(arr, start, piv_pos - 1);    //sorts the left side of pivot.
                QuickSort(arr, piv_pos + 1, end); //sorts the right side of pivot.
            }
        }
        static int partition(int[] arr, int start, int end)
        {
            int i = start - 1;
            int piv = arr[end];            //make the last element as pivot element.
            for (int j = start; j <= end - 1; j++)
            {
                /*rearrange the array by putting elements which are less than pivot
                   on left side and which are greater than pivot on right side. */

                if (arr[j] <= piv)
                {
                    i++;
                    swap(ref arr[i], ref arr[j]);
                }
            }
            swap(ref arr[end], ref arr[i + 1]);  //put the pivot element in its proper place.
            return i + 1;                      //return the position of the pivot
        }
        public static void swap(ref int a, ref int b)
        {
            int temp = a;
            a = b;
            b = temp;
        }       
    }
}
