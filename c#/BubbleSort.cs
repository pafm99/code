using System; 

class BubbleSort {
    static void Main(string[] args) {
		
			Console.WriteLine("Enter the Size of Array");
            int size = int.Parse(Console.ReadLine());  //Read array size.
            Console.WriteLine("Enter the Array elements");

            string[] usrInput = Console.ReadLine().Split(' '); // Read user input seperated by space.

            int[] inputArray = new int[size];

            for (int i = 0; i < size; i++)
            {
                inputArray[i] = int.Parse(usrInput[i]); //Assign user input to array.
            }

            BubbleSort(inputArray);

            Console.WriteLine("The sorted array is ");

            for (int k = 0; k < inputArray.Length; k++)
            {
                Console.Write(inputArray[k] + " "); //Print the sorted array to console.
            }
            Console.ReadLine();
    }
	
	 public static void BubbleSort(int[] arr)
        {
            int size = arr.Length;

            for (int i = 0; i < size; i++)
            {              
                for (int j = 0; j < size - i - 1; j++)
                {
                    if (arr[j] > arr[j + 1])
                    {
						//Swap the elements
                        int temp = arr[j + 1];
                        arr[j + 1] = arr[j];
                        arr[j] = temp;                        
                    }
                }
            }
        }
}
