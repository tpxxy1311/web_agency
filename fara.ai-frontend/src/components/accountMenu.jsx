"use client"
import styles from "@/styles/components/accountMenu.module.scss"
import Link from "next/link";
import Image from "next/image";
import { usePathname } from "next/navigation";

const AccountMenu = () => {

    const pathname = usePathname();

    return ( 
        <Link className={`${styles.accountContainer} ${pathname === '/account' ? styles.active : ''}`} href="/account">
            <Image
                className={styles.accountImage}
                src="/testuser_pb.jpeg"
                alt="Profile Image"
                width={33}
                height={33}
                quality={100}
                unoptimized
            />
            <div className={styles.accountInfo}>
                <p className={styles.userName}>Tim Peters</p>
                <p className={styles.companyName}>HdM</p>
            </div> 
        </Link>
     );
}
 
export default AccountMenu;