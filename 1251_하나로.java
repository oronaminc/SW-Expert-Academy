import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Solution {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer tokens;
	static int T,N;
	static long adjMatrix[][];
	static int [] x,y;
	public static void main(String[] args) throws NumberFormatException, IOException {
		T = Integer.parseInt(br.readLine());
		for(int t=1;t<=T; t++) {
			N = Integer.parseInt(br.readLine());
			int x[] = new int[N];
			tokens = new StringTokenizer(br.readLine(), " ");
			for(int n=0; n<N; n++) x[n] = Integer.parseInt(tokens.nextToken());
			
			int y[] = new int[N];
			tokens = new StringTokenizer(br.readLine(), " ");
			for(int n=0; n<N; n++) y[n] = Integer.parseInt(tokens.nextToken());
			
			adjMatrix = new long[N][N];
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					adjMatrix[i][j] = adjMatrix[j][i] = getDistance(x[i],x[j],y[i],y[j]);
				}
			}// 인접행렬 완성
			double E = Double.parseDouble(br.readLine());
			sb.append("#").append(t).append(" ").append(Math.round(E*makeMST())).append("\n");
		}
		System.out.println(sb);
		
		
		
	}
	private static long makeMST() {
		long minEdge [] = new long[N];
		boolean visited[] = new boolean[N];
		
		long result = 0; // 최소 신장 트리 비용
		int cnt = 0;
		
		Arrays.fill(minEdge, Long.MAX_VALUE);
		minEdge[0] = 0; // 0은 시작점으로!
		
		PriorityQueue<Vertex> pq = new PriorityQueue<>();
		pq.offer(new Vertex(0,minEdge[0]));
		
		while(true) {
			// 1단계 - 신장트리에 포함되지 않는 정점 중에서 최소 간선 비용의 정점을 선택
			// pq를 통해서 자동으로 만들어 집니다.
			Vertex minVertex = pq.poll();
			int minNo = minVertex.no;
			
			if(visited[minNo])continue;
			visited[minNo] = true; // 신장트리에 포함시킴
			result += minVertex.cost;
			if(++ cnt == N)break;
			// 2 단계 - 선택된 정점에서 신장 트리에 포함되지 않는 다른 정점들로부터의 간선 비용을 고려하여 minEdge 업데이트
			for(int i=0; i<N; i++) {
				// 하지만 이 문제는 무조건 간선이 있다고 가정합니다. 그렇기 때문에 중간 조건문은 없애도 됩니다
				if(!visited[i] && adjMatrix[minNo][i]>0 && minEdge[i] > adjMatrix[minNo][i]) {
					minEdge[i] = adjMatrix[minNo][i];
					pq.offer(new Vertex(i,minEdge[i]));
				}
			}
			
		}
		return result;
	}
	static long getDistance(int x1, int x2, int y1, int y2) {
		return (long) (Math.pow(x1-x2, 2)+Math.pow(y1-y2, 2));
	}
	static class Vertex implements Comparable<Vertex>{
		int no;
		long cost;
		public Vertex(int no, long cost) {
			super();
			this.no = no;
			this.cost = cost;
		}
		@Override
		public int compareTo(Vertex o) {
			return Long.compare(this.cost, o.cost);
		}
		
		
	}

}