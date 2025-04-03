"use client"
import styles from "@/styles/components/logo.module.scss"
import Image from "next/image";


const Logo = () => {


    return ( 
        <div className={styles.logoContainer}>
            <Image
            src="/logo.svg"
            width={30}
            height={30}
            className={styles.logoIcon}
            unoptimized
            alt="fara.ai"
            />
            <h4 className={styles.logoText}>fara.ai</h4>
        </div>
     );
}
 
export default Logo;