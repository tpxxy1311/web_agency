import { Outfit } from "next/font/google";
import "./globals.css";
import { cookies } from 'next/headers';
// import Providers from "@/components/provider";


const outfit = Outfit({
  subsets: ["latin"],
  weight: ["300", "400", "500", "600", "700"], 
});

export const metadata = {
  title: "fara.ai",
  description: "fara.ai frontend prototype",
};


export default function RootLayout({ children }) {

  // Holen des Darkmode-Zustands aus den Cookies
  const cookieStore = cookies();
  const darkmode = cookieStore.get('darkmode')?.value === 'true';

  return (
    <html lang="en" data-theme={`${ darkmode ? 'dark' : ''}`}>
      <head>
        <link rel="apple-touch-icon" sizes="180x180" href="favicons/apple-touch-icon.png"/>
        <link rel="icon" href="/favicon.ico"/>  
        <link rel="icon" type="image/png" sizes="32x32" href="favicons/favicon-32x32.png"/>  
        <link rel="icon" type="image/png" sizes="16x16" href="favicons/favicon-16x16.png"/>
        <meta name="theme-color" content="#374B3E"/>
      </head>
      <body className={outfit.className}>
          {children}
      </body>
    </html>
  );
}
