import styles from "@/styles/components/sidebar.module.scss"
import Logo from "./logo";
import MainNavigation from "./mainNavigation";
import HelpNavigation from "./helpNavigation";
import AccountMenu from "./accountMenu";

const Sidebar = () => {
    return ( 
        <div className={styles.sidebar}>
            <div className={styles.topMenu}> 
                <Logo/>
                <MainNavigation/>
            </div>
            <div className={styles.bottomMenu}>
                <HelpNavigation/>
                <AccountMenu/>
            </div>
        </div>
     );
}
 
export default Sidebar;