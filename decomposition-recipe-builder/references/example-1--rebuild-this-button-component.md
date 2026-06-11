### Example 1: Rebuild This Button Component

**Input:**
```jsx
export const PrimaryButton = ({ label, onClick, disabled }) => (
  <button 
    className={`btn btn-primary ${disabled ? 'disabled' : ''}`}
    onClick={onClick}
    disabled={disabled}
  >
    {label}
  </button>
);
```

**Recipe Output:**
```markdown