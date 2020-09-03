package com.ssafy.java.day32;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class s_1767_process_connection {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer tokens;
	static int T,N,L,CNT,MIN;
	static int [][] MAP,CMAP;
	static int DIR [][] = {{-1,0},{1,0},{0,-1},{0,1}};
	static List<pnt> PNT;
	public static void main(String[] args) throws NumberFormatException, IOException {
		T = Integer.parseInt(br.readLine());
		for(int t=1; t<=T; t++) {
			N = Integer.parseInt(br.readLine());
			MAP = new int[N][N];
			PNT = new ArrayList<>();
			for(int r=0; r<N; r++) {
				tokens = new StringTokenizer(br.readLine(), " ");
				for(int c=0; c<N; c++) {
					MAP[r][c] = Integer.parseInt(tokens.nextToken());
					if(MAP[r][c]==1 && r!=0 && r!=N-1 && c != N-1 && c != 0) {
						PNT.add(new pnt(r,c));
					}
				}
				
			}
			L = PNT.size();
			CNT=0;MIN=Integer.MAX_VALUE;
			DFS(MAP,0,0,0);
			sb.append("#").append(t).append(" ").append(MIN).append("\n");
			//System.out.println(MIN);
		}
		System.out.println(sb);

	}
	static void DFS(int[][] map, int cnt, int length, int idx) {
		if(idx==L) {
//			for(int i []: map) {
//				System.out.println(Arrays.toString(i));
//			}
			if(CNT < cnt) {
				CNT = cnt;
				MIN = Integer.MAX_VALUE;
			}
			if(CNT==cnt) MIN = Math.min(MIN, length);
//			System.out.println(cnt+" "+length);
//			System.out.println();
			return;
		}
		
		pnt p = PNT.get(idx);
		
		for(int i=0; i<4; i++) {
			int nR = p.r+DIR[i][0], nC = p.c+DIR[i][1];
			boolean flag = true;
			while(nR>=0 && nR<N && nC>=0 && nC<N) {
				if(map[nR][nC] == 1) {
					flag = false;
					break;
				}
				nR += DIR[i][0];
				nC += DIR[i][1];
			}
			//System.out.println("flag : "+flag);
			if(flag) {
				CMAP = new int[N][N];
				for(int ii=0; ii<N; ii++)	CMAP[ii] = map[ii].clone();
				int l=0;
				int nR2 = p.r+DIR[i][0], nC2 = p.c+DIR[i][1];
				while(nR2>=0 && nR2<N && nC2>=0 && nC2<N) {
					CMAP[nR2][nC2] = 1;
					l++;
					nR2 += DIR[i][0];
					nC2 += DIR[i][1];
				}
				DFS(CMAP,cnt+1, length+l, idx+1);
			}
		}
		DFS(map,cnt,length,idx+1);
		
	}
	static class pnt{
		int r,c;

		public pnt(int r, int c) {
			super();
			this.r = r;
			this.c = c;
		}

		@Override
		public String toString() {
			return "pnt [r=" + r + ", c=" + c + "]";
		}
		
	}

}
