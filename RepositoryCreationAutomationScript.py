from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://repository-app.com/login")  
driver.maximize_window()

# WebDriverWait setup
wait = WebDriverWait(driver, 10)

# Step 1: Log in
username = driver.find_element(By.ID, "username")
wait.until(EC.presence_of_element_located((By.ID, "username")))
username.send_keys("testuser")

password = driver.find_element(By.ID, "password")
wait.until(EC.presence_of_element_located((By.ID, "password")))
password.send_keys("@Password1")

login_btn = driver.find_element(By.ID, "login-btn")
wait.until(EC.element_to_be_clickable((By.ID, "login-btn")))
login_btn.click()

# Step 2: Navigate to Repository Creation Page
create_repo_btn = driver.find_element(By.ID, "create-repo-btn")
wait.until(EC.element_to_be_clickable((By.ID, "create-repo-btn")))
create_repo_btn.click()

# Step 3: Fill repository details
repo_name = driver.find_element(By.ID, "repo-name")
wait.until(EC.presence_of_element_located((By.ID, "repo-name")))
repo_name.send_keys("FirstRepo")

repo_desc = driver.find_element(By.ID, "repo-desc")
wait.until(EC.presence_of_element_located((By.ID, "repo-desc")))
repo_desc.send_keys("This is a test repository")

submit_btn = driver.find_element(By.ID, "submit-btn")
wait.until(EC.element_to_be_clickable((By.ID, "submit-btn")))
submit_btn.click()

# Step 4: Verify repository creation
success_message = driver.find_element(By.CLASS_NAME, "success")
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "success")))

if "Repository created successfully" in success_message.text:
    print("✅ Test Passed: Repository was created successfully!")
else:
    print("❌ Test Failed: Repository creation message not found.")

# Cleanup: Close the browser
driver.quit()
