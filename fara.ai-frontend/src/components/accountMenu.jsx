"use client"
import { userCompanyState, userFirstnameState, userLastnameState } from "@/states/userState";
import styles from "@/styles/components/accountMenu.module.scss"
import { useAtomValue } from "jotai";
import Link from "next/link";
import Image from "next/image";
import { usePathname } from "next/navigation";

const AccountMenu = () => {

    const pathname = usePathname();
    // const firstname = useAtomValue(userFirstnameState);
    // const lastname = useAtomValue(userLastnameState)
    // const company = useAtomValue(userCompanyState);

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
                <p className={styles.userName}>Max Mustermann</p>
                <p className={styles.companyName}>HdM</p>
            </div> 
        </Link>
     );
}
 
export default AccountMenu;