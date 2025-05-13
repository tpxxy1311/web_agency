"use client"
import { Outfit } from "next/font/google";
import styles from "@/styles/global/layout.module.scss"
import Sidebar from "@/components/sidebar";

const outfit = Outfit({
  subsets: ["latin"],
  weight: ["300", "400", "500", "600", "700"], 
});

export default function RootLayout({ children }) {

  return (
      <body className={outfit.className}>
        <Sidebar/>
        <main className={styles.mainContent}>
          {children}
        </main>
      </body>
  );
}