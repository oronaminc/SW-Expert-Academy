import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;
 
public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer tokens;
    static int T, N, r, c, MIN;
    static PNT[] Pnts;
    static boolean visited[];
    public static void main(String[] args) throws NumberFormatException, IOException {
        T = Integer.parseInt(br.readLine());
        for(int t=1; t<=T; t++) {
            N = Integer.parseInt(br.readLine());
            MIN = Integer.MAX_VALUE;
            Pnts = new PNT[N+2];
            visited = new boolean[N+2];
            tokens = new StringTokenizer(br.readLine(), " ");
            r = Integer.parseInt(tokens.nextToken());
            c = Integer.parseInt(tokens.nextToken());
            Pnts[0] = new PNT(r,c);
            r = Integer.parseInt(tokens.nextToken());
            c = Integer.parseInt(tokens.nextToken());
            Pnts[N+1] = new PNT(r,c);
            for(int n=1; n<=N; n++) {
                r = Integer.parseInt(tokens.nextToken());
                c = Integer.parseInt(tokens.nextToken());
                Pnts[n] = new PNT(r,c);
            }
            permu(0, 0, 0);
            sb.append("#").append(t).append(" ").append(MIN).append("\n");
        }
        System.out.println(sb);
    }
     
    static void permu(int index, int cnt, int sum) {
        if(MIN <= sum) return;
        if(cnt == N) {
            sum += (Math.abs(Pnts[index].r-Pnts[N+1].r)+Math.abs(Pnts[index].c-Pnts[N+1].c));
            MIN = Math.min(MIN, sum);
            return;
        }
        for(int idx=1; idx<=N; idx++) {
            if(!visited[idx]) {
                visited[idx] = true;
                permu(idx, cnt+1, sum+Math.abs(Pnts[idx].r-Pnts[index].r)+Math.abs(Pnts[idx].c-Pnts[index].c));
                visited[idx] = false;
            }
        }
    }
     
    static class PNT{
        int r,c;
        public PNT(int r, int c) {
            super();
            this.r = r;
            this.c = c;
        }
    }
}