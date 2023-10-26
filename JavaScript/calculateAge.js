function calculateAge(dateOfBirth) {
    const today = new Date();
    const birthDate = new Date(dateOfBirth);
    
    let age = today.getFullYear() - birthDate.getFullYear();
    const currentMonth = today.getMonth() + 1;
    const birthMonth = birthDate.getMonth() + 1;
  
    if (currentMonth < birthMonth || (currentMonth === birthMonth && today.getDate() < birthDate.getDate())) {
      age--;
    }
  
    return age;
  }
  
  // Example usage:
  const dateOfBirth = "1990-05-15"; // Format: "YYYY-MM-DD"
  const age = calculateAge(dateOfBirth);
  
  console.log(`The age is ${age} years.`);
  