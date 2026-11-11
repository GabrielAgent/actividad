public class actividad{

    public static void main(String[] args) {

        int[] Lista = {64, 25, 12, 22, 11};
        int N = Lista.length;

        for (int i = 0; i < N - 1; i++) {

            int min_indice = i;

            for (int j = i + 1; j < N; j++) {

                if (Lista[j] < Lista[min_indice]) {
                    min_indice = j;
                }
            }

            if (min_indice != i) {
                int aux = Lista[i];
                Lista[i] = Lista[min_indice];
                Lista[min_indice] = aux;
            }
        }
        for (int i = 0; i < N; i++) {
            System.out.print(Lista[i] + " ");
        }
    }
}
