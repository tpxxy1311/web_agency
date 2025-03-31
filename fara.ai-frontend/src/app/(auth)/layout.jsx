"use client";
import { Outfit } from "next/font/google";

const outfit = Outfit({
  subsets: ["latin"],
  weight: ["300", "400", "500", "600", "700"], 
});


export default function RootLayout({ children }) {  

  
  return (
      <body className="__className_a4c6f6">
        {children}
      </body>
  );
}
