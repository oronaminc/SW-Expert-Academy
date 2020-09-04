package com.ssafy.java.day35;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class s_4366_bank {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer tokens;
	static int T, twoL, threeL;
	static long answer, getTwoNum, getThreeNum;
	static String two, three;
	static int [] twoArr, threeArr;
	static boolean FLAG;
	public static void main(String[] args) throws NumberFormatException, IOException {
		T = Integer.parseInt(br.readLine());
		for(int t=1; t<=T; t++) {
			FLAG = false;
			two = br.readLine();
			three = br.readLine();
			twoL = two.length();threeL = three.length();
			twoArr = new int[twoL];	threeArr = new int[threeL];
			for(int i=0; i<twoL; i++)twoArr[i] = two.charAt(i)-'0';
			for(int i=0; i<threeL; i++)threeArr[i] = three.charAt(i)-'0';
			for(int i=0; i<twoL; i++) {
				if(twoArr[i]==0) twoArr[i]=1;
				else if(twoArr[i]==1) twoArr[i]=0;
				
				getTwoNum = getNum(twoArr,2);
				for(int j=0; j<threeL; j++) {
					if(threeArr[j]==0) {
						threeArr[j]=1;
						getThreeNum = getNum(threeArr,3);
						if(getTwoNum==getThreeNum) {FLAG=true; break;}
						threeArr[j]=2;
						getThreeNum = getNum(threeArr,3);						
						if(getTwoNum==getThreeNum) {FLAG=true; break;}
						threeArr[j]=0;
					}else if(threeArr[j]==1) {
						threeArr[j]=0;
						getThreeNum = getNum(threeArr,3);
						if(getTwoNum==getThreeNum) {FLAG=true; break;}
						threeArr[j]=2;
						getThreeNum = getNum(threeArr,3);						
						if(getTwoNum==getThreeNum) {FLAG=true; break;}
						threeArr[j]=1;
					}else if(threeArr[j]==2) {
						threeArr[j]=0;
						getThreeNum = getNum(threeArr,3);
						if(getTwoNum==getThreeNum) {FLAG=true; break;}
						threeArr[j]=1;
						getThreeNum = getNum(threeArr,3);						
						if(getTwoNum==getThreeNum) {FLAG=true; break;}
						threeArr[j]=2;
					}
//					System.out.println(Arrays.toString(twoArr));
//					System.out.println(Arrays.toString(threeArr));
//					System.out.println();

				}		
				
				if(twoArr[i]==0) twoArr[i]=1;
				else if(twoArr[i]==1) twoArr[i]=0;
				if(FLAG)break;
			}
//			System.out.println(getTwoNum+" "+getThreeNum);
			answer = getTwoNum;
			sb.append("#").append(t).append(" ").append(answer).append("\n");
		}
		System.out.println(sb);

	}
	static long getNum(int[] input, int n) {
		long sum=0;int L = input.length;
		for(int i=0;i<L; i++) {
			int num = input[i];
			if(num !=0) sum += (long)(Math.pow(n, L-i-1)*num);
		}
//		System.out.println(">>"+" "+sum+" "+n);
		return sum;
	}

}
