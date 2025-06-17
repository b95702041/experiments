# 🔐 TypeScript Password Generator

A comprehensive, secure password generator built with TypeScript featuring advanced customization options and password strength analysis.

## ✨ Features

- **🎯 Flexible Configuration**: Customize length, character sets, and exclusion rules
- **💪 Strength Analysis**: Built-in password strength checker with scoring system
- **🔄 Bulk Generation**: Generate multiple passwords at once
- **🚫 Smart Exclusions**: Exclude similar or ambiguous characters for better usability
- **🛡️ Security First**: Ensures required character types are always included
- **📊 Detailed Feedback**: Get strength scores and improvement suggestions

## 🚀 Installation

```bash
# Navigate to the password generator directory
cd password-generator

# Install dependencies
npm install

# For development
npm install -g typescript ts-node
```

## 📖 Usage

### Basic Password Generation

```typescript
import { PasswordGenerator, PasswordOptions } from './src/password-generator';

const generator = new PasswordGenerator();

// Strong password with all character types
const strongOptions: PasswordOptions = {
  length: 16,
  includeUppercase: true,
  includeLowercase: true,
  includeNumbers: true,
  includeSymbols: true
};

const password = generator.generate(strongOptions);
console.log('Generated password:', password);
```

### Password Strength Analysis

```typescript
const strength = generator.checkStrength(password);
console.log(`Strength: ${strength.strength} (Score: ${strength.score}/8)`);
console.log('Suggestions:', strength.suggestions);
```

### Bulk Password Generation

```typescript
// Generate 5 passwords with the same options
const passwords = generator.generateMultiple(5, strongOptions);
passwords.forEach((pwd, index) => {
  console.log(`${index + 1}. ${pwd}`);
});
```

### Advanced Configuration

```typescript
// User-friendly password (excludes confusing characters)
const userFriendlyOptions: PasswordOptions = {
  length: 12,
  includeUppercase: true,
  includeLowercase: true,
  includeNumbers: true,
  includeSymbols: false,
  excludeSimilar: true,      // Excludes: i, l, 1, L, o, 0, O
  excludeAmbiguous: true     // Excludes: {}[]()/\`~,;.<>
};

const friendlyPassword = generator.generate(userFriendlyOptions);
```

## ⚙️ Configuration Options

The `PasswordOptions` interface supports the following customization:

| Option | Type | Description | Default |
|--------|------|-------------|---------|
| `length` | `number` | Password length (minimum 1) | Required |
| `includeUppercase` | `boolean` | Include A-Z characters | Required |
| `includeLowercase` | `boolean` | Include a-z characters | Required |
| `includeNumbers` | `boolean` | Include 0-9 characters | Required |
| `includeSymbols` | `boolean` | Include special symbols | Required |
| `excludeSimilar` | `boolean` | Exclude similar chars (i,l,1,L,o,0,O) | Optional |
| `excludeAmbiguous` | `boolean` | Exclude ambiguous chars ({}[]()/\`~,;.<>) | Optional |

## 🔍 Password Strength Scoring

The strength checker evaluates passwords based on:

- **Length** (8+ chars = 1 point, 12+ chars = 2 points)
- **Lowercase letters** (1 point)
- **Uppercase letters** (1 point)  
- **Numbers** (1 point)
- **Special characters** (2 points)
- **No repeated sequences** (1 point)

### Strength Levels
- **8 points**: Very Strong 💪
- **5-7 points**: Strong 👍
- **3-4 points**: Medium ⚠️
- **1-2 points**: Weak ❌
- **0 points**: Very Weak 🔴

## 🏃‍♂️ Running the Code

```bash
# Run with ts-node (development)
npx ts-node src/password-generator.ts

# Or compile and run
npx tsc src/password-generator.ts
node src/password-generator.js
```

### Sample Output
```
🔐 TypeScript Password Generator
================================

📝 Test 1: Strong Password
Password: K8#mP2@vL9$nR7&q
Strength: Very Strong (Score: 8/8)

📝 Test 2: Simple Password
Password: Km8vR9nQ2Lp7
Strength: Strong (Score: 5/8)

📝 Test 3: Multiple Passwords
1. X3#fB7@wE2$kM9&
2. R6*nL4#vK8@tQ1$
3. F9&mJ2#wP5$lN7@
4. B4#kR8*vT6@nM3$
5. L7$wX9#mE4&vK2@

✅ TypeScript Password Generator Complete!
```

## 🧪 Development Status

**Current Status**: ✅ Feature Complete

### ✅ Completed Features
- [x] Flexible password generation
- [x] Character set customization
- [x] Similar/ambiguous character exclusion
- [x] Password strength analysis
- [x] Bulk password generation
- [x] Required character type enforcement
- [x] Comprehensive test examples

### 🔮 Future Enhancements
- [ ] CLI interface
- [ ] Password history tracking
- [ ] Custom word lists integration
- [ ] Export to various formats
- [ ] Entropy calculation
- [ ] Pattern detection

## 🔧 API Reference

### `PasswordGenerator`

#### Methods

- `generate(options: PasswordOptions): string`
  - Generates a single password with specified options
  - Throws error if length < 1 or no character types selected

- `generateMultiple(count: number, options: PasswordOptions): string[]`
  - Generates multiple passwords with the same options
  - Returns array of generated passwords

- `checkStrength(password: string): { score: number; strength: string; suggestions: string[] }`
  - Analyzes password strength and provides feedback
  - Returns detailed strength assessment object

## 📋 Requirements

- Node.js 16+
- TypeScript 4.5+
- npm or yarn

## 🛡️ Security Notes

- Uses `Math.random()` for character selection (suitable for general use)
- For cryptographic applications, consider using `crypto.getRandomValues()`
- Always store generated passwords securely
- Consider the trade-offs between security and usability when excluding characters

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Make your changes and add tests
4. Commit your changes: `git commit -am 'Add new feature'`
5. Push to the branch: `git push origin feature/new-feature`
6. Submit a pull request

## 📄 License

MIT License - see the main repository for details.

---

*Part of the [experiments repository](../README.md)*