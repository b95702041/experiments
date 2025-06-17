console.log('🔐 TypeScript Password Generator');
console.log('================================');

interface PasswordOptions {
  length: number;
  includeUppercase: boolean;
  includeLowercase: boolean;
  includeNumbers: boolean;
  includeSymbols: boolean;
  excludeSimilar?: boolean;
  excludeAmbiguous?: boolean;
}

class PasswordGenerator {
  private readonly uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  private readonly lowercase = 'abcdefghijklmnopqrstuvwxyz';
  private readonly numbers = '0123456789';
  private readonly symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?';
  private readonly similarChars = 'il1Lo0O';
  private readonly ambiguousChars = '{}[]()/\\`~,;.<>';

  generate(options: PasswordOptions): string {
    if (options.length < 1) {
      throw new Error('Password length must be at least 1');
    }

    let charset = this.buildCharset(options);
    
    if (charset.length === 0) {
      throw new Error('At least one character type must be selected');
    }

    let password = '';
    password += this.ensureRequiredChars(options);
    
    for (let i = password.length; i < options.length; i++) {
      const randomIndex = Math.floor(Math.random() * charset.length);
      password += charset[randomIndex];
    }

    return this.shuffleString(password);
  }

  generateMultiple(count: number, options: PasswordOptions): string[] {
    const passwords: string[] = [];
    for (let i = 0; i < count; i++) {
      passwords.push(this.generate(options));
    }
    return passwords;
  }

  checkStrength(password: string): { score: number; strength: string; suggestions: string[] } {
    let score = 0;
    const suggestions: string[] = [];

    if (password.length >= 12) score += 2;
    else if (password.length >= 8) score += 1;
    else suggestions.push('Use at least 8 characters');

    if (/[a-z]/.test(password)) score += 1;
    else suggestions.push('Include lowercase letters');

    if (/[A-Z]/.test(password)) score += 1;
    else suggestions.push('Include uppercase letters');

    if (/[0-9]/.test(password)) score += 1;
    else suggestions.push('Include numbers');

    if (/[^a-zA-Z0-9]/.test(password)) score += 2;
    else suggestions.push('Include special characters');

    if (!/(.)\1{2,}/.test(password)) score += 1;
    else suggestions.push('Avoid repeated characters');

    const strength = this.getStrengthLabel(score);
    return { score, strength, suggestions };
  }

  private buildCharset(options: PasswordOptions): string {
    let charset = '';
    
    if (options.includeUppercase) charset += this.uppercase;
    if (options.includeLowercase) charset += this.lowercase;
    if (options.includeNumbers) charset += this.numbers;
    if (options.includeSymbols) charset += this.symbols;

    if (options.excludeSimilar) {
      charset = charset.split('').filter(char => !this.similarChars.includes(char)).join('');
    }

    if (options.excludeAmbiguous) {
      charset = charset.split('').filter(char => !this.ambiguousChars.includes(char)).join('');
    }

    return charset;
  }

  private ensureRequiredChars(options: PasswordOptions): string {
    let requiredChars = '';
    
    if (options.includeUppercase) {
      let chars = this.uppercase;
      if (options.excludeSimilar) chars = chars.replace(/[O]/g, '');
      requiredChars += this.getRandomChar(chars);
    }
    
    if (options.includeLowercase) {
      let chars = this.lowercase;
      if (options.excludeSimilar) chars = chars.replace(/[il]/g, '');
      requiredChars += this.getRandomChar(chars);
    }
    
    if (options.includeNumbers) {
      let chars = this.numbers;
      if (options.excludeSimilar) chars = chars.replace(/[10]/g, '');
      requiredChars += this.getRandomChar(chars);
    }
    
    if (options.includeSymbols) {
      let chars = this.symbols;
      if (options.excludeAmbiguous) {
        chars = chars.split('').filter(char => !this.ambiguousChars.includes(char)).join('');
      }
      requiredChars += this.getRandomChar(chars);
    }

    return requiredChars;
  }

  private getRandomChar(charset: string): string {
    const randomIndex = Math.floor(Math.random() * charset.length);
    return charset[randomIndex];
  }

  private shuffleString(str: string): string {
    const arr = str.split('');
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr.join('');
  }

  private getStrengthLabel(score: number): string {
    if (score >= 7) return 'Very Strong';
    if (score >= 5) return 'Strong';
    if (score >= 3) return 'Medium';
    if (score >= 1) return 'Weak';
    return 'Very Weak';
  }
}

const generator = new PasswordGenerator();

console.log('\n📝 Test 1: Strong Password');
const strongOptions: PasswordOptions = {
  length: 16,
  includeUppercase: true,
  includeLowercase: true,
  includeNumbers: true,
  includeSymbols: true
};

const strongPassword = generator.generate(strongOptions);
console.log('Password:', strongPassword);

const strength = generator.checkStrength(strongPassword);
console.log('Strength:', strength.strength, '(Score: ' + strength.score + '/8)');

console.log('\n📝 Test 2: Simple Password');
const simpleOptions: PasswordOptions = {
  length: 12,
  includeUppercase: true,
  includeLowercase: true,
  includeNumbers: true,
  includeSymbols: false,
  excludeSimilar: true
};

const simplePassword = generator.generate(simpleOptions);
console.log('Password:', simplePassword);

console.log('\n📝 Test 3: Multiple Passwords');
const passwords = generator.generateMultiple(5, strongOptions);
passwords.forEach((pwd, index) => {
  console.log((index + 1) + '. ' + pwd);
});

console.log('\n✅ TypeScript Password Generator Complete!');
