package com.ssafy.java.day14;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Bean {

	static int T,N,M,CNT;
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer tokens;
	static int MAP[][];
	static int DIR[][] = {{-1,0},{1,0},{0,-1},{0,1}};
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		T = Integer.parseInt(br.readLine());
		for(int t=1;t<=T; t++) {
			tokens = new StringTokenizer(br.readLine(), " ");
			N = Integer.parseInt(tokens.nextToken());
			M = Integer.parseInt(tokens.nextToken());
			MAP = new int[M][N];
			CNT = M*N;
			for(int r=0; r<M; r++) {
				for(int c=0; c<N; c++) {
					if(MAP[r][c] == 0) {
						for(int idx=0; idx<4; idx++) {
							int nr = r+DIR[idx][0]*2;
							int nc = c+DIR[idx][1]*2;
							if(nr>=0 && nr <M && nc >=0 && nc<N && MAP[nr][nc]==0) {
								MAP[nr][nc] = -1;
								CNT--;
							}
							
						}
					}
				}
			}
			sb.append("#").append(t).append(" ").append(CNT).append("\n");
		}
		System.out.println(sb);
		

	}

}
