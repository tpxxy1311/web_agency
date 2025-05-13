"use client";
import { Outfit } from "next/font/google";
import styles from "@/styles/global/layout.module.scss"

const outfit = Outfit({
  subsets: ["latin"],
  weight: ["300", "400", "500", "600", "700"], 
});


export default function RootLayout({ children }) {  

  
  return (
      <body className={outfit.className}>
        <main className={styles.authContent}>
          {children}
        </main>
      </body>
  );
}
