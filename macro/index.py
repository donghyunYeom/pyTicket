# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Chrome 옵션 설정 (user-agent 설정으로 봇 탐지 방지)
options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# 웹드라이버 실행
driver = webdriver.Chrome(options=options)

# 인터파크 로그인 페이지로 이동
driver.get("https://ticket.interpark.com/Gate/TPLogin.asp")

# 카카오 로그인 버튼 클릭
try:
    # 카카오 로그인 버튼이 보이고 클릭 가능할 때까지 대기
    kakao_login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.flex.w-full.flex-row.items-center.justify-center.text-text-neutral-main.typography-subtitle-16-bold"))
    )
    kakao_login_button.click()  # 카카오 로그인 버튼 클릭
    print("카카오 로그인 버튼 클릭!")

    # 팝업 창이 뜰 때까지 대기
    WebDriverWait(driver, 10).until(
        EC.number_of_windows_to_be(2)  # 새 팝업 창이 열리면 2개의 창이 존재
    )

    # 현재 창에서 팝업 창으로 전환
    driver.switch_to.window(driver.window_handles[1])

    # 카카오 로그인 폼이 로드될 때까지 대기
    id_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "id_email_2"))  # 카카오 로그인 아이디 입력 필드 ID
    )
    password_input = driver.find_element(By.ID, "pw_input")  # 카카오 비밀번호 입력 필드 ID

    # 카카오 아이디와 비밀번호 입력
    id_input.send_keys("sunderpower@naver.com")  # 실제 카카오 아이디 입력
    password_input.send_keys("ehdgus14!$")  # 실제 카카오 비밀번호 입력

    # 로그인 버튼 클릭
    login_button = driver.find_element(By.CSS_SELECTOR, "button.submit")  # 카카오 로그인 버튼 CSS 선택자
    login_button.click()

    # 로그인 후 메인 페이지로 돌아갈 때까지 대기
    WebDriverWait(driver, 10).until(
        EC.url_changes("https://accounts.kakao.com/login")
    )
    print("카카오 로그인 완료!")

    # 팝업 창을 닫고 메인 페이지로 돌아옴
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

except Exception as e:
    print(f"로그인 처리 중 오류 발생: {e}")

# 10초 대기 후 브라우저 종료
time.sleep(10)
driver.quit()
