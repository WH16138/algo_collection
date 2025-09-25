#include <iostream>
#include <vector>
using namespace std;

vector<int> pivots; // 피벗 순서 저장 벡터

int medianIndex(vector<int>& arr, int left, int mid, int right) {
    int a = arr[left], b = arr[mid], c = arr[right];
    if ((b <= a && a <= c) || (c <= a && a <= b)) return left;
    if ((a <= c && c <= b) || (b <= c && c <= a)) return right;
    return mid;
} // a, b, c 중 중간값의 인덱스 반환

int partition(vector<int>& arr, int left, int right) {
    int mid = (left + right) / 2;
    int pivotIdx = medianIndex(arr, left, mid, right); // 피벗 인덱스 결정
    swap(arr[left], arr[pivotIdx]); // 피벗을 맨 앞으로 이동
    int pivot = arr[left];
    pivots.push_back(pivot); // 피벗 저장

    int low = left + 1, high = right; // low, high 포인터 초기화
    while (true) {
        while (low <= right && arr[low] < pivot) low++; // 피벗보다 큰 값 찾기
        while (high >= left + 1 && arr[high] > pivot) high--; // 피벗보다 작은 값 찾기
        if (low < high) { // 엇갈리지 않았다면
            swap(arr[low], arr[high]); // 교환
            low++; 
            high--;
        } else break; // 엇갈렸다면 종료
    }
    swap(arr[left], arr[high]); // 피벗을 제자리로 이동
    return high; // 피벗의 최종 위치 반환
}

// 퀵 정렬 함수
void quickSort(vector<int>& arr, int left, int right) {
    if (left >= right) return; // 원소가 1개 이하인 경우 종료
    int p = partition(arr, left, right); // 분할
    quickSort(arr, left, p - 1); // 왼쪽 부분 배열 정렬
    quickSort(arr, p + 1, right); // 오른쪽 부분 배열 정렬
}

int main() {
    // 입출력 최적화
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<int> arr(N); // 정렬할 배열
    for (int i = 0; i < N; i++) cin >> arr[i];

    quickSort(arr, 0, N - 1);

    for (int i = 0; i < (int)pivots.size(); i++) {
        if (i) cout << "_"; 
        cout << pivots[i];
    } // 피벗 선택 순서 출력
    cout << "\n";

    for (int i = 0; i < N; i++) {
        if (i) cout << "_";
        cout << arr[i];
    } // 정렬된 배열 출력
    cout << "\n";
}