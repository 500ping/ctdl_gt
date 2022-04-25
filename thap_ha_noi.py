"""
Cho 3 coc 1, 2, 3. Coc 1 xep 3 dia A, B, C theo thu tu tu lon den be
Chuyen toan bo dia tu coc 1 sang coc 3 theo quy tac
- Moi lan chi duoc chuyen 1 coc
- Khong duoc de dia to nam tren dia nho
"""

def swap(n, a, b):
    print(f'Chuyen dia {n} tu coc {a} --> coc {b}')

def thap_ha_noi(n, coc_1, coc_2, coc_3):
    if n == 1:
        swap(n, coc_1, coc_3)
    else:
        thap_ha_noi(n-1, coc_1, coc_3, coc_2)   # Chuyen n-1 dia sang tu coc thu 1 sang coc thu 2
        swap(n, coc_1, coc_3)                   # Chuyen dia lon nhat sang coc thu 3
        thap_ha_noi(n-1, coc_2, coc_1, coc_3)   # Chuyen n-1 dia tu coc thu 2 sang coc thu 3

thap_ha_noi(3, 1, 2, 3)
