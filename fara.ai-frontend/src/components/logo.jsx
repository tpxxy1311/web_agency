"use client"
import styles from "@/styles/components/logo.module.scss"
import Image from "next/image";
// import { useAtom } from "jotai";
// import { darkmodeState } from "@/states/darkmodeState";


const Logo = () => {

    //const [darkmode, setDarkmode] = useAtom(darkmodeState)

    return ( 
        <div className={styles.logoContainer}>
            <Image
            src={process.env.NEXT_PUBLIC_API_BASE_URL + '/logo.svg'}
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