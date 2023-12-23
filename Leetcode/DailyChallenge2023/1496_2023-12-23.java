import java.util.HashSet;
import java.util.Set;

class Solution {
  public boolean isPathCrossing(String path) {
    Set<String> set = new HashSet<>();
    set.add("0-0");
    int x = 0;
    int y = 0;

    for (char c : path.toCharArray()) {
      switch (c) {
        case 'N':
          y++;
          break;
        case 'S':
          y--;
          break;
        case 'E':
          x++;
          break;
        case 'W':
          x--;
          break;
        default:
          break;
      }

      StringBuilder stringBuilder = new StringBuilder();
      stringBuilder.append(x);
      stringBuilder.append("-");
      stringBuilder.append(y);
      String coords = stringBuilder.toString();

      if (set.contains(coords)) {
        return true;
      }
      set.add(coords);
    }
    return false;
  }
}

