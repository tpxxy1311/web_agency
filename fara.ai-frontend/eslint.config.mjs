import { dirname } from "path";
import { fileURLToPath } from "url";
import { FlatCompat } from "@eslint/eslintrc";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const compat = new FlatCompat({
  baseDirectory: __dirname,
});

const eslintConfig = [
  // Ignorierte Verzeichnisse
  {
    ignores: ["**/.next/**", "**/node_modules/**", "**/public/**"]
  },

  // Importierte Regeln aus klassischen Configs (Next.js, React, Hooks)
  ...compat.extends(
    "next/core-web-vitals",
    "plugin:react/recommended",
    "plugin:react-hooks/recommended"
  ),

  // Eigene Regeln und Einschränkung auf bestimmte Dateien
  {
    files: ["src/**/*.{js,jsx}"], // ← entscheidend!
    rules: {
      // Recommended Base Rules
      "no-unused-vars": "warn",
      "no-console": "warn",
      "no-empty-function": "warn",
      "complexity": ["warn", { max: 5 }],
      "max-lines": ["warn", 300],
      "max-lines-per-function": ["warn", 50],
      // React Rules
      "react/react-in-jsx-scope": "off",
      "react/prop-types": "off"
    },
    settings: {
      react: {
        version: "detect"
      }
    }
  }
];

export default eslintConfig;
