import java.io.File;
import java.util.Arrays;
import java.util.Comparator;

class Solution {
    static class File {
        String fineName;
        String head;
        int number;

        public File(String fineName, String head, int number) {
            this.fineName = fineName;
            this.head = head;
            this.number = number;
        }
    }
    public static String[] solution(String[] files) {

        File[] fileArr = new File[files.length];

        for (int i = 0; i< files.length; i++) {
            String[] divided = divideFileName(files[i]);
            fileArr[i] = new File(files[i], divided[0], Integer.parseInt(divided[1])); 
        }
        
        Arrays.sort(fileArr, new Comparator<File>() {
            @Override
            public int compare(File o1, File o2) {
                if((o1.head).equals(o2.head)) return o1.number - o2.number; // 헤드가 같으면 number 오름차순
                else return (o1.head).compareTo(o2.head); // 아니면 head 기준 정렬
            }
        });
        
        String[] result = new String[files.length];
        for (int i = 0; i < files.length; i++) {
            result[i] = fileArr[i].fineName;
        }
        
        return result;

    }

    // file 을 head, number, tail 나눠서 배열로 리턴 
    public static String[] divideFileName(String fileName) {
        String[] split = new String[3];
        split[0] = "";
        split[1] = "";
        split[2] = "";
        int index = 0;

        for (int i = 0; i < fileName.length(); i++) {
            char temp = fileName.charAt(i);

            if (index == 0 && !Character.isDigit(temp)) {
                split[index] += temp;
                continue;
            }
            if (index == 0 && Character.isDigit(temp)) {
                index++;
            }
            if (index == 1 && Character.isDigit(temp)) {
                split[index] += temp;
                continue;
            }
            if (index == 1 && !Character.isDigit(temp)) {
                index++;
            }
            split[index] += temp;
        }
        split[0] = split[0].toLowerCase();
        
        return split;
    }
}
