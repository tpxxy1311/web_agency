# Structured Requirements Document  

## Functional Requirements  

### Core Functionalities  
1. **Email Input Field**  
   - Must accept user input.
   - Basic validation: Checks if the field is left empty or contains an invalid email format.  
   - Displays inline error messages beneath the field for validation issues.  

2. **Password Input Field**  
   - Must accept user input.  
   - Input should be obscured for privacy.  
   - Basic validation: Checks if the field is left empty.  
   - Displays inline error messages beneath the field for validation issues.  

3. **Login Button**  
   - Triggers form submission logic.  
   - Validates all input fields upon click.  
   - If login credentials are invalid, displays a form-level error message above input fields.  

4. **Registration Link**  
   - Redirects users to the "/register" page if clicked.  

### User Actions  
- Enter an email and password to log in.  
- Receive feedback for any missing or invalid inputs.  
- Click the Login button to submit credentials.  
- Navigate to registration page via the link if not registered.  

### API Calls  
- **/login**  
  - Invoked upon form submission via the Login button.  

## Non-functional and Design Requirements  

### Layout  
- Two-column design with equal 50% division.  
- **Left Column**:  
  - Branding panel with a peacock background image.  
  - Includes a dark green overlay gradient from top to bottom.  
  - Image occupies three quarters of the left column.  
  - Rounded corners.  
- **Right Column**:  
  - Login form, centered vertically and horizontally.  
  - Heading and instruction text at the top.  
  - Vertically stacked input fields with consistent spacing.  

### Visual Preferences  
- **Login Form Header**: "Login to your Account"  
- **Instruction Text**: "Please enter the account details to get to your fara.ai Dashboard."  
- **Icons**:  
  - **Email Input**: MUI EmailOutlined icon.  
  - **Password Input**: MUI LockOutlined icon.  
  - Icons embedded inside input elements.  
- **Login Button**:  
  - Primary green with white text and a white icon.  
- **Registration Text**:  
  - "You don't have an Account? Register your company here"  
  - The registration link text is clickable.  

## UX and Accessibility Considerations  

### Contrast and Visibility  
- Branding image and overlay must ensure adequate contrast for text and UI elements.  
- Button and icons must be visually distinctive for clarity.  

### Keyboard Navigation  
- All form fields, buttons, and links must be fully navigable via keyboard controls.  
- Ensure logical tab order for intuitive navigation.  

### Screen Reader Accessibility  
- All form fields, labels, and messages should be properly labeled for screen readers.  
- Error messages must be announced by screen readers upon appearance.  

### Responsiveness  
- The page must be responsive to different screen sizes, maintaining usability and readability on desktop and mobile devices.  

This detailed structured document ensures that designers and developers have clear, actionable guidance for creating a responsive and accessible login page.