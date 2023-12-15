import java.util.List;
import java.util.ArrayList;

// a HashMap solution would be faster

class Solution {
    public String destCity(List<List<String>> paths) {
        List<String> starting = new ArrayList<>();
        List<String> destinations = new ArrayList<>();

        for (int i=0; i<paths.size(); i++){
            starting.add(paths.get(i).get(0));
            destinations.add(paths.get(i).get(1));
        }

        destinations.removeAll(starting);

        String final_dest = destinations.get(0);

        return final_dest;
    }
}